# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd


labels = ['opacity', 'normal']
# reading larger image size might slow down the process
img_size = 150


def load_pneumonia_data(data_dir):
    data = []
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):

            try:
                # set images to grayscale
                img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                resized_arr = cv2.resize(img_arr, (img_size, img_size))

                data.append([resized_arr, class_num])

            # if anything fails, the 'except' will print error message
            except Exception as e:
                print(e)
    # convert images to array to easier in model
    return np.array(data, dtype="object")


train = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\train")
test = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test")


def display_images():
    # figsize is set in inches
    plt.figure(figsize=(5, 5))
    plt.imshow(train[0][0], cmap="hot")   # cmap = colormap
    plt.title(labels[train[0][1]])

    plt.figure(figsize=(5, 5))
    plt.imshow(train[-1, 0], cmap="hot")
    plt.title(labels[train[-1, 1]])

    plt.show()


# first to normalize the images and create a training, and test sets
# doing this will help machine learning model for accurate results and
# better weights


x_train = []
y_train = []

x_test = []
y_test = []

for feature, label in train:
    x_train.append(feature)
    y_train.append(label)

for feature, label in test:
    x_test.append(feature)
    y_test.append(label)


# normalize data
x_train = np.array(x_train) / 255.0
x_test = np.array(x_test) / 255.0

# we normalize images to improve contrast and making it better for processing
# resize data
x_train = x_train.reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)

x_test = x_test.reshape(-1, img_size, img_size, 1)
y_test = np.array(y_test)

