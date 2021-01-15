#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:55:05 2020
@author: GlobeEater
Reads images into the trained model and outputs predictions.
"""
from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img, save_img
from Model_Builder_2 import get_model, get_data, display_mask
from keras.models import load_model
import os
import PIL
from PIL import ImageOps
import tensorflow as tf
from tensorflow import keras
import numpy as np

def predictor():
    # Read in data
    input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Unclassified/"
    img_size = (160, 160)
    batch_size = 32
    num_classes = 2
    
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
    model = get_model(img_size, num_classes)
    model.load_weights("/Users/kellenbullock/Desktop/Natural_Resources_Project/models/rotation_gen_10000.h5")
    
    # Save Results with numerical ordering:
    images = []
    for i, num in enumerate(x):
        val_preds = model.predict(x)
        mask = np.argmax(val_preds[i], axis=-1)
        mask = np.expand_dims(mask, axis=-1)
        img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
        images.append(img)
        display(img)
    
    n = 0
    for i in input_img_paths:
        for j in images:
            j.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/predictions/" + str(i[77:-4]) + "_" + str(n) + ".png")
            n = n + 1
            if n > 14:
                n = 0
                
if __name__ == '__main__':
    predictor()