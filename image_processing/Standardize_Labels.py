import os
import ctypes
from ctypes import *
libstdimg = CDLL("./libstdimg.so")

# Calling the C function to check connection
libstdimg.connect()

input_dir = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Stage_1/"

input_img_paths = sorted(
        [
             os.path.join(input_dir, fname)
             for fname in os.listdir(input_dir)
             if fname.endswith(".jpg")
         ]
    )
image_standardize = libstdimg.std_image
image_standardize.argtypes = (ctypes.c_char_p, ctypes.c_char_p)

for i in input_img_paths:
    path_1 = i
    print(i)
    print("path 1 = %s", path_1)
    path_2 = '/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Stage_2/' + str(i[72:-4]) + "_" + '.png'
    print("path2 = %s", path_2)
    print("")
    path_1 = path_1.encode('utf-8')
    path_2 = path_2.encode('utf-8')
    image_standardize(path_1, path_2)
    print("done.")
