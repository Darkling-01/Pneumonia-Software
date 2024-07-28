import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential, Model
from preprocessing import blur_train, blur_test, blur_val


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

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.dense1(x)
        return self.dense2(x)


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


