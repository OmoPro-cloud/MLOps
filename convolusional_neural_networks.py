#Convolutional Neural Network (CNN)
  #Convolutional Layer(this layers purpose is feature extraction)
  #Pooling Layer(this layers works is downsampling, reduces the size of the feature maps, making the layer faster)
  #Flatten Layer(converts the 2d feature maps into 1D vectors)
  #Dense Layer()

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

#Load Fashion MNIST dataset of clothing images. It is built into keras
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

#normalize 0-1 range
x_train = x_train / 255.0
x_test = x_test / 255.0

#reshape to include channel dimensions (grayscale = 1 channel)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

#Label name for reference
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#Visualize some clothing images
plt.figure(figsize=(8, 8))
for i in range(9):
  plt.subplot(3, 3, i + 1)
  plt.imshow(x_train[i].reshape(28, 28), cmap='gray')
  plt.title(class_names[y_train[i]])
  plt.axis('off')
plt.show()

#Build the CNN model