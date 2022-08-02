# -*- coding:utf-8 -*-

import os
import random
import shutil
from PIL import Image

def shrink(file,output_path):
    img=file
    img2=img.resize((256,256))
    img2.save(output_path)

def crop_img(input_path,output_path): # input&output_path is the file_folder name

    for filename in os.listdir(input_path):
        im=Image.open(os.path.join(input_path,filename))

        img_size=im.size # tuple(width,height)
        new_width=442

        num_name=filename.split(";")[0]
        input=im.crop((163,67,163+new_width,67+new_width))
        output=output_path+"/"+num_name+"_ep.png"
        shrink(input, output)

    return


def main():
    project_dir=os.path.dirname(os.path.abspath(__file__)) # get filefolder abs_name
    origin=os.path.join(project_dir,'dataset','test_env_point_render_png')
    # output=os.path.join(project_dir,'dataset','env_point_render_cropped')
    output="/home/xh/cjm/envTopoint/test_env_point_render_cropped"
    crop_img(origin,output)

    origin2=os.path.join(project_dir,'dataset','test_point_render_png')
    #output2=os.path.join(project_dir,'dataset','test_point_render_cropped')
    output2="/home/xh/cjm/envTopoint/test_point_render_cropped"
    crop_img(origin2,output2)

main()
    