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

                # calls the function to rotate the images
                # rotated_arr = image_rotation(resized_arr)

                # adding the corresponding label to each image
                data.append([resized_arr, class_num])

            except Exception as e:
                print(f"Error: {e}")

    # convert images to array to easily process in model
    return data


# load each dataset
train = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\train")
test = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test")
val = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\val")


# ---------------------
# | data augmentation |
# ---------------------
def image_rotation(data):
    augmented_data = []
    for image, label in data:
        augmented_data.append([image, label])

        # create a simple rotation for 90, 180, 270 degrees
        rotation_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        rotation_180 = cv2.rotate(image, cv2.ROTATE_180)
        rotation_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # each rotation will add the corresponding labels
        augmented_data.append([rotation_90, label])
        augmented_data.append([rotation_180, label])
        augmented_data.append([rotation_270, label])

        return augmented_data


# establishing the image rotation
augmented_train = image_rotation(train)
augmented_test = image_rotation(test)
augmented_val = image_rotation(val)

# implement a function to enhance blurry images and noises.
# using the Gaussian Kernel to smooth out the images
def image_blurring(data):


