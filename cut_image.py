# -*- coding:utf-8 -*-

import os
import random
import shutil
from PIL import Image

""" 
def choose_train(input_path,output_path):
    img=os.listdir(input_path) # all data
    picknumber=1000
    sample=random.sample(img,picknumber) # return name of chosen file
    for name in sample:
        shutil.copy(input_path+'/'+name,output_path+'/'+name)
    return
 """


def crop_img(input_path,output_path):

    for filename in os.listdir(input_path):
        im=Image.open(os.path.join(input_path,filename))

        img_size=im.size # tuple(width,height)

        new_width=img_size[0]/5
        new_height=img_size[1]

        num_name=filename.split(";")[0]
        input=im.crop((0,0,new_width,new_height))
        input_name=num_name+"_input.png"
        input.save(output_path+"/"+input_name)

        normal=im.crop((new_width,0,new_width*2,new_height))
        normal_name=num_name+"_normal.png"
        normal.save(output_path+"/"+normal_name)

        diffuse=im.crop((new_width*2,0,new_width*3,new_height))
        diffuse_name=num_name+"_diffuse.png"
        diffuse.save(output_path+"/"+diffuse_name)

        roughness=im.crop((new_width*3,0,new_width*4,new_height))
        roughness_name=num_name+"_roughness.png"
        roughness.save(output_path+"/"+roughness_name)

        specular=im.crop((new_width*4,0,new_width*5,new_height))
        specular_name=num_name+"_specular.png"
        specular.save(output_path+"/"+specular_name)
    return



def main():
    project_dir=os.path.dirname(os.path.abspath(__file__)) # get filefolder abs_name
    origin=os.path.join(project_dir,'testBlended')
    # chosn=os.path.join(project_dir,'1000_train')
    output=os.path.join(project_dir,'dataset','test_cropped')
    # choose_train(origin,chosn)
    crop_img(origin,output)

main()
    