import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential, load_model

from preprocessing import blur_train, blur_test, blue_val


# preparing images for machine learning model
def encode_images(load_path):
    

