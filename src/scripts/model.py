import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential, load_model
from preprocessing import blur_train, blur_test, blur_val


class CNN(tf.keras.models):
    def __int__(self):
        super(CNN, self).__int__()
        self.conv1 = Conv2D()


# technique used to represent categorical data, such as our class labels. Each category is assigned a
# unique binary code
# e.g. NORMAL or OPACITY
def encode_images(load_path, classes):
    encoded = tf.keras.utils.to_categorical(load_path, classes)

    return encoded

