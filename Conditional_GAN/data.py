# -*- coding: utf-8 -*-

import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

from PIL import Image

from settings import *

class AttrDataset(Dataset):

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.attr_list = self.read(csv_file)
        self.root_dir = root_dir
        self.transform = transform
    def read(self,csv_file):
        res = pd.read_csv(csv_file)
        res = res.drop(columns = ['Unnamed: 0'])
        return res



    def __len__(self):
        return len(self.attr_list)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.attr_list.ix[idx, 0])
        image = Image.open(img_name)
        attrs = self.attr_list.iloc[idx, 1:].values.astype('float')
        attrs = torch.FloatTensor(attrs)

        if self.transform:
            image = self.transform(image)

        return image, attrs


face_transform = transforms.Compose([
           transforms.Resize(128),
           transforms.RandomHorizontalFlip(),
           transforms.ToTensor(),
       ])

