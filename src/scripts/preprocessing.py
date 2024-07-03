# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import os
import cv2
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

# global variables
labels = ['normal', 'opacity']
img_size = 150

DELAY_CAPTION = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31


def load_pneumonia_data(data_dir):
    # empty object will store dataset(s) when compiled
    data = []
    # will loop through images in folders labeling them respectfully
    for label in labels:
        PATH = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(PATH):
            try:
                # convert the images to grayscale
                img_arr = cv2.imread(os.path.join(PATH, img), cv2.IMREAD_GRAYSCALE)
                # resizing the images can improve speed but loses quality
                resized_arr = cv2.resize(img_arr, (img_size, img_size))
                # adding the corresponding label to each image
                data.append([resized_arr, class_num])

            except Exception as e:
                print(f"Error: {e}")

    # convert images to array to easily process in model
    return np.array(data, dtype='object')


# load each dataset
train = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\train")
test = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test")
val = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\val")


# Gaussian Filter, the most useful but not the fastest
def smoothing_images(data):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv2.GaussianBlur(data, (i, i), 0)
        return dst

