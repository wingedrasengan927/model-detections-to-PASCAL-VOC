# model-detections-to-PASCAL-VOC

This project helps to semi-automate the labelling process for object detection model by converting the raw detections made by the pre-trained tensorflow object detection model to xml files in PASCAL VOC format. The xml files and the images can the be loaded into an annotation tool. The user then has to just tweak the bounding boxes and save making the process easier.

## Setup

first clone this repository into your machine and then clone the tensorflow models directory into this directory, and follow the installation instructions for the object detection model given there.
the models repository can be found here https://github.com/tensorflow/models

## How to use 

After setup, put the image you want to use into the 
'''
input_images
'''
