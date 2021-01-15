#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:08:55 2020

This will train a ML classifier model to detect Cedar Trees.

@author: GlobeEater
"""

import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image
import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend" # Deleteing the first @ will use the gpu if configured prior.
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import time

input_data = "/Users/kellenbullock/Desktop/square_trees.png"
target_data = "/Users/kellenbullock/Desktop/Labels_3.png"
img_size = (584, 584)
num_classes = 2
batch_size = 32

X = load_img(input_data, target_size=img_size)
Y = load_img(target_data, img_size, color_mode="grayscale")

X = tf.keras.preprocessing.image.img_to_array(X)
Y = tf.keras.preprocessing.image.img_to_array(Y)

independents = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
m = independents.reshape(-1, 584, 584, 3) #np.expand_dims(X, 2)
    
dependents = np.zeros((batch_size,) + img_size + (1,), dtype="uint8")
n = dependents.reshape(-1, 584, 584, 1) #np.expand_dims(Y, 2)

x_train, x_test, y_train, y_test = train_test_split(m, n, test_size=0.2, random_state=42)

model = Sequential()
model.add(   Conv2D(32, (3,3), input_shape = (x_train.shape[1:])))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3)))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

start = time.time()
model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1)

score = model.evaluate(x_test, y_test, batch_size=32)
model.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/Cedar_classifier.h5")
print(score)
end = time.time()
print("time to run: ", end - start)