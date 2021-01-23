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
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import layers
import re

def get_data():
    input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Training_Img_Color"
    target_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Training_Img_Label"
    img_size = (160, 160)
    num_classes = 2
    batch_size = 140
    
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
    
    images = np.zeros((batch_size,) + img_size + (3,), dtype="float32")
    for j, path in enumerate(input_img_paths):
        img = load_img(path, target_size=img_size)
        images[j] = img
    masks = np.zeros((batch_size,) + img_size + (1,), dtype="uint8")
    for j, path in enumerate(target_img_paths):
        img = load_img(path, target_size=img_size, color_mode="grayscale")
        masks[j] = np.expand_dims(img, 2)

    return images, masks, img_size, num_classes, batch_size, input_img_paths, target_img_paths

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

def display_mask(i, val_preds):
        """Quick utility to display a model's prediction."""
        mask = np.argmax(val_preds[i], axis=-1)
        mask = np.expand_dims(mask, axis=-1)
        img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
        display(img)

def main():
    images, masks, img_size, num_classes, batch_size, input_img_paths, target_img_paths = get_data()
    # Build model
    model = get_model(img_size, num_classes)
    
    datagen = ImageDataGenerator(width_shift_range=[-5,5], height_shift_range=[-5,5],
    vertical_flip=True,horizontal_flip=True, rotation_range=45, shear_range=0.1,
    zoom_range=[-0.2, 0.2], brightness_range=[-0.25, 0.25])   
        # width_shift_range=[-15,15],vertical_flip=True,horizontal_flip=True
    it = datagen.flow(images, masks)
    
    model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy")
    callbacks = [keras.callbacks.ModelCheckpoint("Tree_segmentation.h5", save_best_only=True)]
    model.fit(it, epochs=5, callbacks=callbacks, verbose=1) # validation_data=val_gen, 
    #model = tf.keras.models.load_model("/Users/kellenbullock/Desktop/Natural_Resources_Project/Tree_segmentation.h5")
    val_preds = model.predict(it)
        
    # Display results for validation image #
    i = 8
    # Display input image
    display(Image(filename=input_img_paths[i]))
    # Display ground-truth target mask
    img = PIL.ImageOps.autocontrast(load_img(target_img_paths[i]))
    display(img)
    # Display mask predicted by our model
    display_mask(i, val_preds)  # Note that the model only sees inputs at 160x160.
if __name__ == '__main__':
    main()