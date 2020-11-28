#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:36:51 2020

@author: kellenbullock
"""
import os
from IPython.display import Image, display
from PIL import Image

input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Raw_Sliced_Images/"

input_img_paths = sorted(
    [
         os.path.join(input_data_path, fname)
         for fname in os.listdir(input_data_path)
         if fname.endswith(".png")
     ]
)

def get_concat_h(im1, im2, im3, im4):
    dst = Image.new('RGB', (im1.width + im2.width + im3.width + im4.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    dst.paste(im4, (im1.width + im2.width + im3.width, 0))
    return dst

img_1 = Image.open(input_img_paths[0])
img_2 = Image.open(input_img_paths[1])
img_3 = Image.open(input_img_paths[4])
img_4 = Image.open(input_img_paths[5])
new = get_concat_h(img_1, img_2, img_3, img_4)
new.show()

for i in input_img_paths:
    # slice path names and create lists for each picture
    temp = i[0][82:]
    site = temp[:4]
    
    # divide sites
    picture = []
    if temp in i:
       picture.append(i)
    assert len(picture) < 15
        
    # save each site out
    
        
#x = Image.open(i)
#y = Image.open(i = 1) 
    

# Iterate over row one and concat

# Iterate over second row and concat

# Itareate over third row and concat

# Concat all three rows together 
