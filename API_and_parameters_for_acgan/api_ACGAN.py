import shutil
import numpy as np
import torch
from models import *



def load_model():
	#Get the pretrained Model
	generator = Generator()
	generator.apply(weights_init)
	checkpoint = torch.load('./models/Epoch:_058.pt')
	generator.load_state_dict(checkpoint['g_state_dict'])
	generator = generator.cuda()
	return generator




def edit(tar):
	# factor to edit 
    allone = [1.0 for i in range(32)]
    allzero =[0.0 for i in range(32)]
    out = []
    for i in tar:
        tmp = []
        for j in range(4):
            if j == i:
                tmp += allzero
            else:
                tmp += allone
        out.append(tmp)
    out = torch.FloatTensor(out)
    return out.cuda()


def get_image(model,target):
	# model is the model get from load_model
	# target is a 1xbatch_size numpy_array or list
    
    tags = torch.FloatTensor(target).cuda()
    target = np.array(target)
    batch_size = target.shape[0]
    embedding = nn.Embedding(batch_size,128).cuda()
    max_tag = np.argmax(target,axis = 1)
  
    z = Variable(torch.FloatTensor(batch_size, 128))
    z = z.cuda()
    z.data.fill_(0.0)
    z.data.normal_(0, 1)

    tag = torch.LongTensor(max_tag).cuda()
    #embed = embedding(tag).view(batch_size,-1).cuda()
    #xx = z.mul(embed)
    factor = edit(max_tag)
    x = z.mul(factor)
    print(x.data)
    print(tags.data)
    
    rep = torch.cat((x, tags.clone()), 1)
    print(rep.data[0])
    fake = model.forward(rep).detach()
    return fake.cpu().data.numpy()