import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, Input
from keras.models import Sequential, Model, load_model
from keras.preprocessing import image

from src.scripts.preprocessing import X_train, X_test, y_train, y_test, X_val, y_val

from datetime import datetime as dt
import numpy as np


class CNN(Model):
    def __init__(self):
        super(CNN, self).__init__()
        # first convolutional layer
        self.conv1 = Conv2D(32, 4, activation='relu', padding='same')   # 'same' with zero padding
        # first pooling layer
        self.pool1 = MaxPooling2D(2)
        # second convolutional layer
        self.conv2 = Conv2D(64, 4, activation='relu', padding='same')
        # second pooling layer
        self.pool2 = MaxPooling2D(2)
        # Flatten layer to convert 2D feature maps to 1D
        self.flatten = Flatten()
        # First fully connected (dense) layer
        self.dense1 = Dense(120, activation='relu')
        # Output layer with softmax activation for classification
        self.dense2 = Dense(10, activation='softmax')

    def call(self, input_tensor):
        x = self.conv1(input_tensor)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.dense1(x)
        return self.dense2(x)


def train_model(X_train, y_train, X_val, y_val):
    # input shape (150 x 150 with channel)
    # grayscale images use channel: 1
    # RGB images use channel: 3
    input_layer = Input(shape=(150, 150, 1))
    x = CNN()(input_layer)

    model = Model(inputs=input_layer, outputs=x)
    # print(model.summary(expand_nested=True))

    # specify training configuration(optimizer, loss, metrics)
    model.compile(
        optimizer=keras.optimizers.RMSprop(),
        # used when there are two or more label classes
        loss=keras.losses.SparseCategoricalCrossentropy(),
        # list of metrics to monitor
        metrics=['accuracy']
    )

    # call fit() to train the model by slicing into "batches"
    history = model.fit(
        X_train,
        y_train,
        batch_size=256,
        epochs=2,
        # we pass some validation for
        # monitoring validation loss and metrics
        # at the end of each epoch
        validation_data=(X_val, y_val)
    )

    # Return the last accuracy value
    final_accuracy = history.history['accuracy'][-1] if 'accuracy' in history.history else None
    return final_accuracy


# compute how long it takes the training model to finish
def training_time(X_train, y_train, X_val, y_val):
    start = dt.now()
    # process the model time
    final_accuracy = train_model(X_train, y_train, X_val, y_val)
    end = dt.now()
    running_secs = (end - start).total_seconds()

    return final_accuracy, running_secs


accuracy, duration = training_time(X_train, y_train, X_val, y_val)
# print(f"Training Time: {duration:.2f} seconds")


def preprocess_image(img_path, target_size=(150, 150)):
    # preprocess the input image suitable for model prediction
    img = load_model(img_path, target_size=target_size, color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.append(img_array, axis=0)    # add batch dimension
    img_array = img_array / 255

    return img_array

def predict_image(img_path, model):
    

