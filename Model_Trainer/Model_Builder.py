#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:02:57 2020

@author: kellenbullock
"""

from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img
import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import PIL
from PIL import ImageOps
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import layers
import random
import re

input_data_path = "/Users/kellenbullock/Desktop/Training_Img_Color"
target_data_path = "/Users/kellenbullock/Desktop/Training_Img_Label"
img_size = (160, 160)
num_classes = 2
batch_size = 2

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


# Combining 
input_img_paths = sorted(
    [
         os.path.join(input_data_path, fname)
         for fname in os.listdir(input_data_path)
         if fname.endswith(".png")
     ]
)

target_img_paths = sorted(
    [
         os.path.join(target_data_path, fname)
         for fname in os.listdir(target_data_path)
         if fname.endswith(".png")
     ]
)

input_img_paths = natural_sort(input_img_paths)
target_img_paths = natural_sort(target_img_paths)
#print("Number of samples:", len(input_img_paths))
#for input_path, target_path in zip(input_img_paths, target_img_paths):
#    print(input_path, "|", target_path)

class Cedar_Trees(keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays)."""

    def __init__(self, batch_size, img_size, input_img_paths, target_img_paths):
        self.batch_size = batch_size
        self.img_size = img_size
        self.input_img_paths = input_img_paths
        self.target_img_paths = target_img_paths

    def __len__(self):
        return len(self.target_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_img_paths = self.input_img_paths[i : i + self.batch_size]
        batch_target_img_paths = self.target_img_paths[i : i + self.batch_size]
        x = np.zeros((batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_input_img_paths):
            img = load_img(path, target_size=self.img_size)
            x[j] = img
        y = np.zeros((batch_size,) + self.img_size + (1,), dtype="uint8")
        for j, path in enumerate(batch_target_img_paths):
            img = load_img(path, target_size=self.img_size, color_mode="grayscale")
            y[j] = np.expand_dims(img, 2)
        return x, y

''' Backup plan:
X = load_img(input_data, target_size=img_size, interpolation='nearest')
Y = load_img(target_data, target_size=img_size, color_mode="grayscale", interpolation='nearest')

X = tf.keras.preprocessing.image.img_to_array(X)
Y = tf.keras.preprocessing.image.img_to_array(Y)

independents = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
independents = independents.reshape(-1, 480, 480, 3) #np.expand_dims(X, 2)
    
dependents = np.zeros((batch_size,) + img_size + (1,), dtype="float32")
dependents = dependents.reshape(-1, 480, 480, 1) #np.expand_dims(Y, 2)
'''

def get_model(img_size, num_classes):
    inputs = keras.Input(shape=img_size + (3,))

    ### [First half of the network: downsampling inputs] ###

    # Entry block
    x = layers.Conv2D(32, 3, strides=2, padding="same")(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    # Blocks 1, 2, 3 are identical apart from the feature depth.
    for filters in [64, 128, 256]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(filters, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    ### [Second half of the network: upsampling inputs] ###

    for filters in [256, 128, 64, 32]:
        x = layers.Activation("relu")(x)
        x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.UpSampling2D(2)(x)

        # Project residual
        residual = layers.UpSampling2D(2)(previous_block_activation)
        residual = layers.Conv2D(filters, 1, padding="same")(residual)
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    # Add a per-pixel classification layer
    outputs = layers.Conv2D(num_classes, 3, activation="softmax", padding="same")(x)

    # Define the model
    model = keras.Model(inputs, outputs)
    return model


# Build model
model = get_model(img_size, num_classes)

# Split our img paths into a training and a validation set
val_samples = 6
random.Random(8).shuffle(input_img_paths)
random.Random(8).shuffle(target_img_paths)
train_input_img_paths = input_img_paths[:-val_samples]
train_target_img_paths = target_img_paths[:-val_samples]
val_input_img_paths = input_img_paths[-val_samples:]
val_target_img_paths = target_img_paths[-val_samples:]

# Create dataset:
train_gen = Cedar_Trees(batch_size, img_size, input_img_paths, target_img_paths)
val_gen = Cedar_Trees(batch_size, img_size, val_input_img_paths, val_target_img_paths)

model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy")
callbacks = [keras.callbacks.ModelCheckpoint("Tree_segmentation.h5", save_best_only=True)]
model.fit(train_gen, epochs=25, validation_data=val_gen, callbacks=callbacks, verbose=1)


val_preds = model.predict(val_gen)

def display_mask(i):
    """Quick utility to display a model's prediction."""
    mask = np.argmax(val_preds[i], axis=-1)
    mask = np.expand_dims(mask, axis=-1)
    img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
    display(img)
    
# Display results for validation image #10
i = 2
# Display input image
display(Image(filename=val_input_img_paths[i]))
# Display ground-truth target mask
img = PIL.ImageOps.autocontrast(load_img(val_target_img_paths[i]))
display(img)
# Display mask predicted by our model
display_mask(i)  # Note that the model only sees inputs at 150x150.

