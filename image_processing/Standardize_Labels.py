import os

input_dir = "/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Stage_2/"

input_img_paths = sorted(
        [
             os.path.join(input_data_path, fname)
             for fname in os.listdir(input_data_path)
             if fname.endswith(".jpg")
         ]
    )
for x in input_img_paths:
    
