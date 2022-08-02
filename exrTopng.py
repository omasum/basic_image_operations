# coding:utf-8
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
import numpy as np


def exrTopng(filename_exr,filrname_png):
    img = cv2.imread(filename_exr,cv2.IMREAD_UNCHANGED)
    img=img*65535
    img[img>65535]=65535
    img=np.uint16(img)
    cv2.imwrite(filrname_png,img)

def main():
    filename_exr=r"G:\mitsuba\examplescene\single_image\dataset\test_point_render"
    file=os.listdir(filename_exr)
    for f in file:
        exr_path=os.path.join(filename_exr,f)
        num=f.split(";")[0]
        filename_png=r"G:\mitsuba\examplescene\single_image\dataset\test_point_render_png\%s;p.png" % num
        print(filename_png)
        exrTopng(exr_path,filename_png)

main()