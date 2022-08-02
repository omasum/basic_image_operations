from os import path
import cv2
import numpy as np

path=r"F:\code\Python\my_project\envTopoint\red.png"
img=cv2.imread(path)
print(img[0][0])