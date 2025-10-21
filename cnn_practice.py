#BUILD A CNN WITH 3 DIFFERENT ARCHITECTURES

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

#normalize range from 0 - 1
x_train = x_train / 255.0
x_test = x_test / 255.0

#reshape the values to include a grayscale channel(allows color)
x_train = x_train.reshape(1, 28, 28, -1)
x_test = x_test.reshape(1, 28, 28, -1)

