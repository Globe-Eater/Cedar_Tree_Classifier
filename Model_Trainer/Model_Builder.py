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

input_data = "/Users/kellenbullock/Desktop/square_trees.jpg"
target_data = "/Users/kellenbullock/Desktop/Labels_2.png"
img_size = (480, 480)
num_classes = 2
batch_size = 32

X = load_img(input_data, target_size=img_size, interpolation='nearest')
Y = load_img(target_data, target_size=img_size, color_mode="grayscale", interpolation='nearest')

X = tf.keras.preprocessing.image.img_to_array(X)
Y = tf.keras.preprocessing.image.img_to_array(Y)

independents = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
independents = independents.reshape(-1, 480, 480, 3) #np.expand_dims(X, 2)
    
dependents = np.zeros((batch_size,) + img_size + (1,), dtype="float32")
dependents = dependents.reshape(-1, 480, 480, 1) #np.expand_dims(Y, 2)

### Creation of lists training : target data:

### object creation:


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

model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy")
callbacks = [keras.callbacks.ModelCheckpoint("Tree_segmentation.h5", save_best_only=True)]
model.fit(x=independents, y=dependents, epochs=10, callbacks=callbacks, verbose=1)

val_data = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/raw_images/Z2S3.jpg"
validation = load_img(val_data, target_size=img_size, interpolation='nearest')

display(validation)
v = tf.keras.preprocessing.image.img_to_array(validation)

validation = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
validation = validation.reshape(-1, 480, 480, 3) #np.expand_dims(X, 2)

val_preds = [dependents]

#val_preds.append(model.predict(validation))
result = model.predict(validation)
test = result.reduce

mask = np.argmax(val_preds[1], axis=-1)
mask = np.expand_dims(mask, axis=-1)
img = keras.preprocessing.image.array_to_img(mask)
display(img)


