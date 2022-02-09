#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:01:15 2022

@author: user
"""
from ffcv.loader import Loader, OrderOption
from ffcv.fields.decoders import NDArrayDecoder
from ffcv.transforms import ToTensor
import os

batch_size = 16
num_workers = 16
ORDERING = OrderOption.RANDOM

PIPELINES = {
  'img': [NDArrayDecoder(), ToTensor()],
  'ldx': [NDArrayDecoder(), ToTensor()],
  'ldy': [NDArrayDecoder(), ToTensor()],
  'output': [NDArrayDecoder(), ToTensor()]
}

path0 = os.getcwd()
path = os.path.join(path0, 'ffcv_data', 'dummy_dataset_train.beton')
ORDERING = OrderOption.RANDOM

loader = Loader(path,
                batch_size=batch_size,
                num_workers=num_workers,
                order=ORDERING,
                drop_last=False,
                distributed = False,
                # seed=0,
                os_cache=False,
                pipelines=PIPELINES)