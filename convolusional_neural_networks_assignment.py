import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

# Load Fashion MNIST dataset of clothing images (built into Keras)
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()


#Comparing pixel ranges BEFORE normalization
print("Before normalization:")
print("Max pixel value:", np.max(x_train))
print("Min pixel value:", np.min(x_train))

#Normalize to 0-1 range
x_train = x_train / 255.0
x_test = x_test / 255.0

#Comparing pixel ranges AFTER normalization
print("\nAfter normalization:")
print("Max pixel value:", np.max(x_train))
print("Min pixel value:", np.min(x_train))

#Reshape to include channel dimension (grayscale = 1 channel)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Label names for reference
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#Show 12 random images from training dataset
plt.figure(figsize=(10, 6))
random_indices = np.random.choice(len(x_train), size=12, replace=False)
for i, idx in enumerate(random_indices):
    plt.subplot(3, 4, i + 1)
    plt.imshow(x_train[idx].reshape(28, 28), cmap='gray')
    plt.title(class_names[y_train[idx]])
    plt.axis('off')
plt.suptitle("12 Random Images from Training Data", fontsize=16)
plt.tight_layout()
plt.show()


#Display images using inferno color map

plt.figure(figsize=(10, 6))
for i, idx in enumerate(random_indices):
    plt.subplot(3, 4, i + 1)
    plt.imshow(x_train[idx].reshape(28, 28), cmap='inferno')
    plt.title(class_names[y_train[idx]])
    plt.axis('off')
plt.suptitle("12 Images with 'inferno' Color Map", fontsize=16)
plt.tight_layout()
plt.show()

# Observation (manually describe in your report/notebook):
# Using color maps like 'inferno' or 'viridis' can enhance contrast
# and make features more visible compared to plain grayscale.

#Inspect one image (e.g., x_train[0])
image_index = 0
image = x_train[image_index]
label = y_train[image_index]
print("\nInspecting image at index 0:")
print("Image shape:", image.shape)
print("Pixel values (flattened):", image.reshape(-1)[:100], "...")
print("Label:", class_names[label])


#Custom title experiment (image index + label)

plt.figure(figsize=(10, 6))
for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.imshow(x_train[i].reshape(28, 28), cmap='plasma')
    plt.title(f"Image {i}: {class_names[y_train[i]]}")
    plt.axis('off')
plt.suptitle("Images with Index and Class Name", fontsize=16)
plt.tight_layout()
plt.show()
