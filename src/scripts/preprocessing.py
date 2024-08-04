# convert the raw data into a clean data set before feeding it
# to the algorithm in model
import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split

# global variables
labels = ['normal', 'opacity']
img_size = 150
limit = 4000


def load_pneumonia_data(data_dir, limit_1=None):
    # empty object will store dataset(s) when compiled
    data = []
    # will loop through images in folders labeling them respectfully
    for label in labels:
        PATH = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(PATH):
            if limit_1 and len(data) >= limit_1:
                return data

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
    return data


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

    # convert to numpy array
    augmented_data = np.array(augmented_data, dtype=object)

    return augmented_data


# implement a function to enhance blurry images and noises.
# using the Gaussian Kernel to smooth out the images
def image_blurring(data):
    blur = []
    for image, label in data:
        blur.append([image, label])
        cleaned = cv2.GaussianBlur(image, (5, 5), 0)

        blur.append([cleaned, label])

    blur = np.array(blur, dtype=object)

    return blur


# load datasets
train = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\train", limit)
test = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test", limit)
val = load_pneumonia_data(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\val", limit)

# Augment data
augmented_train = image_rotation(train)
augmented_test = image_rotation(test)
augmented_val = image_rotation(val)

# Blur data
blurred_train = image_blurring(augmented_train)
blurred_test = image_blurring(augmented_test)
blurred_val = image_blurring(augmented_val)


# Convert to arrays for splitting
def split_features_labels(data):
    images = np.array([item[0] for item in data])
    classes = np.array([item[1] for item in data])
    return images, classes


X_train, y_train = split_features_labels(blurred_train)
X_test, y_test = split_features_labels(blurred_test)
X_val, y_val = split_features_labels(blurred_val)

# perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=42)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=42)

