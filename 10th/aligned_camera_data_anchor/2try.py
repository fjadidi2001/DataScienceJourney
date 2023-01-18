# import the modules
import os
from os import listdir

# get the path/directory
folder_dir = "C:/Users/RIJUSHREE/Desktop/Gfg images"
for images in os.listdir(folder_dir):

    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)