import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential, Model
from preprocessing import blur_train, blur_test, blur_val


class CNN(Model):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = Conv2D(32, 4, activation='relu', padding='same')
        self.pooling = MaxPooling2D(2)
        self.flatten = Flatten()
        self.fc1 = Dense(120, activation='relu')
        self.fc2 = Dense(2, activation='softmax')  # assuming 2 classes for the output

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.pooling(x)     # pooling is used to shrink input images
        x = self.flatten(x)
        x = self.fc1(x)

        return self.fc2(x)


# technique used to represent categorical data, such as our class labels. Each category is assigned a
# unique binary code
# e.g. NORMAL or OPACITY
def preprocess_images(images, target_size=(128, 128)):
    images_resized = tf.image.resize(images, target_size)
    images_normalized = images_resized / 255.0

    return images_normalized


images_preprocessed = preprocess_images(blur_train)

model = CNN()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
