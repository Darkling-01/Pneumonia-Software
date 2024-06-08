# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import pandas as pd
import os


TRAIN_PATH = os.listdir(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\train")
TEST_PATH = os.listdir(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test")


def fetch_pneumonia_data():

    try:
        for images in TRAIN_PATH:
            print("Folders: ", images)

    except EOFError as e:
        print("Fix Error: ", e)


