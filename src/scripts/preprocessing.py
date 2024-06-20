# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam


labels = ['opacity', 'normal']
# reading larger image size might slow down the process
img_size = 150

epochs = 14
batchSize = 32


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
val = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\val")

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

x_val = []
y_val = []


for feature, label in train:
    x_train.append(feature)
    y_train.append(label)

for feature, label in test:
    x_test.append(feature)
    y_test.append(label)

for feature, label in val:
    x_val.append(feature)
    y_val.append(label)

# we normalize images to improve contrast and making it better for processing
# normalize data
x_train = np.array(x_train) / 255.0
x_test = np.array(x_test) / 255.0
x_val = np.array(x_val) / 255.0

# resize data

# -1 means to adjust this dimension to make data fit
# 1 means to reshape array to 1 column

x_train = x_train.reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)

x_test = x_test.reshape(-1, img_size, img_size, 1)
y_test = np.array(y_test)

x_val = x_val.reshape(-1, img_size, img_size, 1)
y_val = np.array(y_val)

# create data augmentation
datagen = ImageDataGenerator(
    featurewise_center=False,                 # set input to 0 (zero) over the dataset
    samplewise_center=False,                  # set each sample to 0
    featurewise_std_normalization=False,      # divide inputs by STD of the dataset
    samplewise_std_normalization=False,       # divide each input by its STD
    zca_whitening=False,                      # Apply zca whitening
    rotation_range=30,                        # degree range for random rotations
    zoom_range=0.2,                           # random zoom
    width_shift_range=0.1,                    # range for random horizontal shifts
    height_shift_range=0.1,                   # range for random vertical shifts
    horizontal_flip=True,                     # randomly flips inputs horizontally
    vertical_flip=False                       # randomly flips inputs vertically
)

datagen.fit(x_train)


# creating the model using the sequential API
model = keras.models.Sequential([

    # padding set to 'same' uses zero padding
    # strides is used to skip some instances
    keras.layers.Conv2D(32, 3, strides=1, padding='same',
                        activation='relu', input_shape=(150, 150, 1)),
    # pooling layers goal is to subsample (shrink) the input image to reduce computational load, and the memory usage
    keras.layers.MaxPool2D((2, 2), strides=2, padding='same'),
    keras.layers.Dropout(0.2),     # using dropout with a rate of 20% each to avoid over-fitting

    keras.layers.Conv2D(64, 3, strides=1, padding='same', activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.MaxPool2D((2, 2), strides=2, padding='same'),

    keras.layers.Conv2D(128, 3, strides=1, padding='same', activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.MaxPool2D((2, 2), strides=2, padding='same'),

    # Flatten() use to transform multi-dimensional feature to single-dimensional vector
    keras.layers.Flatten(),
    keras.layers.Dense(units=64, activation='relu'),    # expects a 1D array of features for each instance
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units=1, activation='sigmoid')

])

# set optimizer
optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)

# configure the model process before training the model
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# fit the model
history = model.fit(datagen.flow(x_train, y_train, batch_size=batchSize), epochs=epochs,
                    validation_data=datagen.flow(x_val, y_val))
