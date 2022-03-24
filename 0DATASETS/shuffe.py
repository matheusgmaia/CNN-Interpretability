import os
import random
import shutil


files_list = []

for root, dirs, files in os.walk("/home/maia/Documents/Universidade/Universidade/UNIVERSIDADE/EXPERIMENTO/0DATASETS/OCT/OCT/train"):
    for file in files:
        #all 
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            files_list.append(os.path.join(root, file))


#print images
#lets me count and print the amount of jpeg,jpg,pmg 
file_count = len(files_list)
print(file_count)
random.shuffle(files_list)


dict_folders = {"CNV":37205, "DME":11348, "DRUSEM":8616, "NORMAL":51140}
destPath = "/home/maia/Documents/Universidade/Universidade/UNIVERSIDADE/EXPERIMENTO/0DATASETS/OCT/OCT_RANDOM/train/"
i = 0
for key, value in dict_folders.items():
    destPathN = destPath + key
    os.mkdir(destPathN)
    for x in range(i, i + value, 1):
        shutil.copy(files_list[x], destPathN)
    i = i + value
