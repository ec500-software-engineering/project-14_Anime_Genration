# -*- coding: utf-8 -*-

import torch

DATA_PATH = './extra_data/images/'
#DATA_PATH = './faces'
resume_file = ''
cuda = torch.cuda.is_available()
batch_size = 64
z_dim = 128
tag_num = 4
imsize = 128
start_epoch = 0
max_epochs = 50
lambda_adv = tag_num
lambda_gp = 0.5
learning_rate = 0.0002
