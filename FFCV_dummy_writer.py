#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:14:16 2022

@author: user
"""

import numpy as np
from ffcv.writer import DatasetWriter
from ffcv.fields import NDArrayField
from dataset import dataset
import os
import time

s = time.time()

num=2

datasets ={
    'train' : dataset(num, is_train=True),
    'test':  dataset(num, is_train=False)}

path0 = os.getcwd()

for (name, ds) in datasets.items(): 
    # print('loaded', name)
                               
    writer = DatasetWriter(os.path.join(path0, 'ffcv_data', f'dummy_dataset_{name}.beton'), {
        'img': NDArrayField(shape=(2, 60, 60), dtype=np.dtype('float32')),
        'ldx': NDArrayField(shape=(10,1, 60, 60), dtype=np.dtype('float32')),
        'ldy': NDArrayField(shape=(10, 1, 60, 60), dtype=np.dtype('float32')),
        'output': NDArrayField(shape=(10,1,60,60), dtype=np.dtype('float32')),
        }, page_size=4294967296, num_workers=48)   
    writer.from_indexed_dataset(ds)

# page_size=4294967296: 409 MB

e = time.time()
print('running time:', e-s)