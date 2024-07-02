# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam


labels = ['normal', 'opacity']
img_size = 150


def load_pneumonia_data(data_dir):
    # empty object will store dataset(s) when compile
    data = []
    # will loop through images in folders labeling them respectfully
    for label in labels:
        PATH = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(data_dir):
            try:
                


