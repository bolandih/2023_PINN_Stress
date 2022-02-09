#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:24:04 2021

@author: user
"""
import os
from scipy.io import loadmat
import numpy as np
from skimage import io
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset


def loader(idx, label, path0=os.getcwd()):
    
    if label == 'img':
        path = os.path.join(path0,  "dummy_data_input", f"{idx}")
        for i in range(2):
            image = io.imread(os.path.join(path,f'{i}.png'))[:,:,0]/255.             
            # image = image - 0.5 / 0.5
            if i == 0:
                geo = image
                # print('geo',geo.shape)                
            else:
                bc = image                 
                # print('bc',bc.shape)               
                img = np.dstack((geo,bc))
                img = np.transpose(img,(2,0,1))           
                # print('img:', img.shape)
                                
        return img
      
    if label == 'load_x':
       path_lx = os.path.join(path0,  "dummy_data_input", f"{idx}", f"{2}.mat")    
       load_x = loadmat(path_lx, squeeze_me=True)['my_list']        
       load_x =  load_x.reshape(-1,1,60,60)     
       # print('load_x :',load_x.shape)
       return load_x
   
    if label == 'load_y': 
       path_ly = os.path.join(path0,  "dummy_data_input", f"{idx}", f"{3}.mat")   
       load_y = loadmat(path_ly ,squeeze_me=True)['my_list'] 
       load_y =  load_y.reshape(-1,1,60,60)
       # print('load_y :',load_y.shape)
       return load_y
   
    if label == 'output':
       path_output = os.path.join(path0,  "dummy_data_output", f"Y{idx+1}.mat")   
       output = loadmat(path_output,squeeze_me=True)['my_list'] #Ar,data
       # output = np.transpose(output,(2,0,1))
       output =  output.reshape(-1,1,60,60)
       # print('output :',output.shape)
       return output
                                                                         

class dataset(Dataset):
    def __init__(self, num, path0=os.getcwd(), train_ratio = 0.8, 
                 is_train=True, loader=loader):

        self.train_list, self.test_list = train_test_split(np.arange(num), 
                                                           train_size=train_ratio, 
                                                           random_state=42)
        self.is_train = is_train
        self.loader = loader
            
    def __len__(self):
        if self.is_train is True:
            return len(self.train_list)
        else:
            return len(self.test_list)
    
    def __getitem__(self, idx):
        if self.is_train is True:
            fidx = self.train_list[idx]
            train_image = self.loader(fidx, 'img').astype('float32')            
            train_load_x = self.loader(fidx, 'load_x').astype('float32')
            train_load_y = self.loader(fidx, 'load_y').astype('float32')
            train_output = self.loader(fidx, 'output').astype('float32') # already is float32
            # train_image = [0]
            # train_output = [0]
            # train_load_x= [0]
            # train_load_y= [0]
            return train_image, train_load_x,train_load_y,train_output
        
        else:
            fidx = self.test_list[idx]
            test_image = self.loader(fidx, 'img').astype('float32')   
            # print('test_image',np.shape(test_image))
            test_load_x = self.loader(fidx, 'load_x').astype('float32')   
            # print('test_load_x:',test_load_x.shape)
            test_load_y = self.loader(fidx, 'load_y').astype('float32')   
            test_output = self.loader(fidx, 'output').astype('float32')
            # print('test_output',test_output.shape)
            return test_image, test_load_x, test_load_y,test_output  