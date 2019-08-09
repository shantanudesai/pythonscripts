# -*- coding: utf-8 -*-

import os
from collections import Counter
path = input("Path to the folder you want to analyse ( Make sure to use forwardslash e.g C:/Users/XXX/Downloads/YYY): ")
os.chdir(path)
print("Current working dir : %s"% os.getcwd())
extensions = []
for f in os.listdir():
    file_name,file_ext = os.path.splitext(f)
    extensions.append(file_ext)
extensions.sort()
extn_name = list(Counter(extensions).keys())
extn_num = list(Counter(extensions).values())

for i in range (0,len(extn_name)):
    print("There are",extn_num[i]," files with type",extn_name[i])
