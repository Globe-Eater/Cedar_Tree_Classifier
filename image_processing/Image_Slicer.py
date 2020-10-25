#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:36:51 2020

@author: kellenbullock
"""

from IPython.display import Image, display
from PIL import Image

input_data = "/users/kellenbullock/Desktop/Labels.png"
big_img = Image.open(input_data)

#big_img.show()
# left, up, right, bottom

# First row
left = 86
up = 104
right = 160 + 86 
bottom = 160 + 104


for (i = 0; i <= 960; i + 160):
    dims = (left + i, up, right + i, bottom)
    secs = big_img.crop(dims)
    sections.append(secs)

# Second Row

left = 86
up = 160 + 104
right = 160 + 86
bottom= 320 + 104

for (i = 0; i <= 960; i + 160):
    dims = (left + i, up, right + i, bottom)
    secs = big_img.crop(dims)
    sections.append(secs)

# Third Row

left = 86
up = 320 + 104
right = 160 + 86
bottom = 480 + 104
for (i = 0; i <= 960; i + 160):
    dims = (left + i, up, right + i, bottom)
    secs = big_img.crop(dims)
    sections.append(secs)

i = 0
for i in sections:
    sec = sectionss[i]
    sec.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/labeled_images/Z2S3_" + i + ".png")
    
    
#dims = (left, up, right, bottom)
#    # Cropping tool
#secs = big_img.crop(dims)
#secs.show()
#sections = []