#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:36:51 2020
@author: kellenbullock
"""
import os
from IPython.display import Image, display
from PIL import Image

def concat_images():
    input_data_path = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/predictions/"
    
    input_img_paths = sorted(
        [
             os.path.join(input_data_path, fname)
             for fname in os.listdir(input_data_path)
             if fname.endswith(".png")
         ]
    )
    
    def get_concat_h(im1, im2, im3, im4, im5):
        dst = Image.new('RGB', (im1.width + im2.width + im3.width + im4.width + im5.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        dst.paste(im3, (im1.width + im2.width, 0))
        dst.paste(im4, (im1.width + im2.width + im3.width, 0))
        dst.paste(im5, (im1.width + im2.width + im3.width + im4.width, 0))
        return dst
    
    def get_concat_v(row1, row2, row3):
        dst = Image.new('RGB', (row1.width, row1.height + row2.height + row3.height))
        dst.paste(row1, (0, 0))
        dst.paste(row2, (0, row1.height))
        dst.paste(row3, (0, row1.height + row2.height))
        return dst
    
    #img_1 = Image.open(input_img_paths[0])
    #img_2 = Image.open(input_img_paths[1])
    #img_3 = Image.open(input_img_paths[2])
    #img_4 = Image.open(input_img_paths[3])
    #img_5 = Image.open(input_img_paths[4])
    #new = get_concat_h(img_1, img_2, img_3, img_4, img_5)
    #new.show()
    
    # slice path names and create lists for each picture
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thriteen = []
    fourteen = []
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = []
    nineteen = []
    twenty = []
    twenty_one = []
    twenty_two = []
    twenty_three = []
    twenty_four = []
    twenty_five = []
    twenty_six = []
    twenty_seven = []
    twenty_eight = []
    twenty_nine = []
    thirty = []
    thirty_one = []
    thirty_two = []
    thirty_three = []
    thirty_four = []
    
    Zones =  [one, two, three, four, five, six, seven, eight, nine, ten ,eleven, twelve,\
              thriteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty,\
              twenty_one, twenty_two, twenty_three, twenty_four, twenty_five, twenty_six, \
              twenty_seven, twenty_eight, twenty_nine, thirty, thirty_one, thirty_two, thirty_three,
              thirty_four]
    
    for i in input_img_paths:
        temp = i[76:-6]
        site = temp[:4]
        # divide sites
        if site == 'Z1S1':
            one.append(i)
        if site == 'Z1S2':
            two.append(i)
        if site == 'Z1S3':
            three.append(i)
        if site == 'Z1S4':
            four.append(i)
        if site == 'Z1S5':
            five.append(i)
        if site == 'Z1S6':
            six.append(i)
        if site == 'Z1S7':
            seven.append(i)
        if site == 'Z1S8':
            eight.append(i)
        if site == 'Z1S9':
            nine.append(i)
        if site == 'Z2S1':
            ten.append(i)
        if site == 'Z2S2':
            eleven.append(i)
        if site == 'Z2S3':
            twelve.append(i)
        if site == 'Z2S4':
            thriteen.append(i)
        if site == 'Z2S5':
            fourteen.append(i)
        if site == 'Z2S6':
            fifteen.append(i)
        if site == 'Z2S7':
            sixteen.append(i)
        if site == 'Z2S8':
            seventeen.append(i)
        if site == 'Z2S9':
            eighteen.append(i)
        if site == 'Z3S1':
            nineteen.append(i)
        if site == 'Z3S2':
            twenty.append(i)
        if site == 'Z3S3':
            twenty_one.append(i)
        if site == 'Z3S4':
            twenty_two.append(i)
        if site == 'Z3S5':
            twenty_three.append(i)
        if site == 'Z3S4':
            twenty_four.append(i)
        if site == 'Z3S5':
            twenty_five.append(i)
        if site == 'Z3S6':
            twenty_six.append(i)
        if site == 'Z4S1':
            twenty_seven.append(i)
        if site == 'Z4S2':
            twenty_eight.append(i)
        if site == 'Z4S3':
            twenty_nine.append(i)
        if site == 'Z4S4':
            thirty.append(i)
        if site == 'Z4S5':
            thirty_one.append(i)
        if site == 'Z4S6':
            thirty_two.append(i)
        if site == 'Z4S7':
            thirty_three.append(i)
        if site == 'Z4S8':
            thirty_four.append(i)
            
    # Sorting pictures by numerical order
    for x in Zones:
        for i in x:
            pic_num = i[81:]
            # row 1
            if pic_num == '0.png':
                img_1 = Image.open(i)
            if pic_num == '1.png':
                img_2 = Image.open(i)
            if pic_num == '2.png':
                img_3 = Image.open(i)
            if pic_num == '3.png':
                img_4 = Image.open(i)
            if pic_num == '4.png':
                img_5 = Image.open(i)
            # row 2
            if pic_num == '5.png':
                img_6 = Image.open(i)
            if pic_num == '6.png':
                img_7 = Image.open(i)
            if pic_num == '7.png':
                img_8 = Image.open(i)
            if pic_num == '8.png':
                img_9 = Image.open(i)
            if pic_num == '9.png':
                img_10 = Image.open(i)
            # row 3
            if pic_num == '10.png':
                img_11 = Image.open(i)
            if pic_num == '11.png':
                img_12 = Image.open(i)
            if pic_num == '12.png':
                img_13 = Image.open(i)
            if pic_num == '13.png':
                img_14 = Image.open(i)
            if pic_num == '14.png':
                img_15 = Image.open(i)
    
    row1 = get_concat_h(img_1, img_2, img_3, img_4, img_5)
    #row1.show()
    row2 = get_concat_h(img_6, img_7, img_8, img_9, img_10)
    #row2.show()
    row3 = get_concat_h(img_11, img_12, img_13, img_14, img_15)
    #row3.show() 
    # final concat:
    final = get_concat_v(row1, row2, row3)
    final.show()
    final.save("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Raw_Sliced_Images2/" + str(i[76:-4]) + ".png")

if __name__ == '__main__':
    concat_images()