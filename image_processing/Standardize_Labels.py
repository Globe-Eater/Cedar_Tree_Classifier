import os
import ctypes

input_dir = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Stage_2/"

input_img_paths = sorted(
        [
             os.path.join(input_data_path, fname)
             for fname in os.listdir(input_dir)
             if fname.endswith(".jpg")
         ]
    )
standardizer = ctypes.CDLL("standard_process.so")
standardizer.standardize.argtypes = [ctypes.c_wchar_p]

for x in input_img_paths:
    standardizer.standardize(x, "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Raw_Sliced_Images/" + str(x[77:-4]) + "_" + str(n) + ".png")

