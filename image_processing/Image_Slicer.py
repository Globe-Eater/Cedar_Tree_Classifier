#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:36:51 2020
@author: kellenbullock
"""
import os
from IPython.display import Image, display
from PIL import Image

def image_slicer():
    input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Color_Stage/"
    
    input_img_paths = sorted(
        [
             os.path.join(input_data_path, fname)
             for fname in os.listdir(input_data_path)
             if fname.endswith(".jpg")
         ]
    )
    
    for x in input_img_paths:
        big_img = Image.open(x)
        
        sections = []
        # First row
        left = 86
        up = 104
        right = 160 + 86 
        bottom = 160 + 104
        
        i = up
        while i <= 3252:
            dims = (left + i, up, right + i, bottom)
            secs = big_img.crop(dims)
            sections.append(secs)
            i = i + 160
        # Second Row
        left = 86
        up = 160 + 104
        right = 160 + 86
        bottom= 320 + 104
        
        i = up
        while i <= 3252:
            dims = (left + i, up, right + i, bottom)
            secs = big_img.crop(dims)
            sections.append(secs)
            i = i + 160
        # Third Row
        
        left = 86
        up = 320 + 104
        right = 160 + 86
        bottom = 480 + 104
        
        i = up
        while i <= 3252:
            dims = (left + i, up, right + i, bottom)
            secs = big_img.crop(dims)
            sections.append(secs)
            i = i + 160
        n = 0
        for i in sections:
            i.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Training_Img_Color/" + str(x[76:-4]) + "_" + str(n) + ".png")
            #little_img.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/labeled_images/Z2S3_" + str(i) + ".png")
            n += 1
if __name__ == '__main__':
    image_slicer()
    #dims = (left, up, right, bottom)
    #    # Cropping tool
    #secs = big_img.crop(dims)
    #secs.show()
    #sections = []
