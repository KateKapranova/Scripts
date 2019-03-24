#script to iterate over files in subdirectories to find specific file names
#files satisfying the search query are copied into the destination folder
#for Windows OS

import os
from shutil import copy


directory="C:\\Users\\Kapranova\\Documents\\KDEF_and_AKDEF\\KDEF"
dst= "C:\\Users\\Kapranova\\Documents\\KDEF_and_AKDEF\\KDEF\\Front"

for subdir in os.listdir(directory):
    if subdir != "Front":
        for file in os.listdir(os.path.join(directory,subdir)):
            if file.endswith("S.JPG"):
                source=os.path.join(directory,subdir,file)
                copy(source,dst)
            else:
                continue
