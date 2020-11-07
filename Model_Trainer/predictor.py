#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:55:05 2020

@author: GlobeEater
Reads images into the trained model and outputs predictions.
"""

from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img, save_img
import os
import PIL
from PIL import ImageOps
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Read in data
input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Unclassified/"
img_size = (160, 160)
batch_size = 32

input_img_paths = sorted(
    [
         os.path.join(input_data_path, fname)
         for fname in os.listdir(input_data_path)
         if fname.endswith(".jpg")
     ]
)
# Load in images
x = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
for j, path in enumerate(input_img_paths):
            img = load_img(path, target_size=img_size)
            x[j] = img

# load saved model:
model = tf.keras.models.load_model('/Users/kellenbullock/Desktop/Natural_Resources_Project/Tree_segmentation.h5', custom_objects=None, compile=True)
    
for i, num in enumerate(x):
    results = model.predict(x)
    save_img("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/predictions/img_" + str(input_data_path[77:-4]) + "_" +  str(num) + ".png", results)
    

    