#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:08:55 2020

This will train a ML classifier model to detect Cedar Trees.

@author: GlobeEater
"""

import pandas as pd
import tensorflow as tf
from PIL import image
import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend" # Deleteing the first @ will use the gpu if configured prior.
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
import time


image = tf.keras.preprocessing.image.load_img("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/raw_images/Z3S3 copy.jpg")
training_data = tf.keras.preprocessing.image.img_to_array(image)

# Train/Test split
independents = training_data 
dependent = pd.read_csv("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Labels.csv")

x_train, x_test, y_train, y_test = train_test_split(independents, dependent, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=independents.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

start = time.time()
history = model.fit(x_train, y_train, validation_split=0.25, epochs=20, batch_size=32, verbose=1)

score = model.evaluate(x_test, y_test, batch_size=64)
model.save('/users/kellenbullock/desktop/shpo/SAVED_MODELS/Propname_Address_LOCATION_model.h5')
print(score)
end = time.time()
print("time to run: ", end - start)