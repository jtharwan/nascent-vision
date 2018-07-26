# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:29:47 2018
@author: Jay
This file is a image resizing script
I take the input image and resize them to 300x300

"""

#importing opencv and os
import cv2
import os

#Read and write directories . Note empty folders
#need to be created to populate the resized images
#datadir = "/home/jay/Tensorflow/Jay/bikes"
#writeto = "/home/jay/Tensorflow/Jay/bikes_resized"

datadir = "../bikes"
writeto = "../bikes_resized"


#List the number of directories in the bikes directory
subdir = os.listdir(datadir)

#Size used to count the number of images 
size = 0

#Calculate number of image files
for dir in subdir:
    images = os.listdir(datadir + '/' + dir)
    size += len(images)
    
i = 0

#Read the files , resize them and write it to the writeto directory 
for dir in subdir:
    images = os.listdir(datadir + '/' + dir)
    for image in images:
        img = cv2.imread(datadir + '/' + dir + '/' + image)
        imgresized = cv2.resize(img, (300, 300))
        cv2.imwrite(writeto+ '/' + dir + '/' + image, imgresized)
        i = i+1
