import tensorflow as ts
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

#load the dataset
(x_train, x_test), (y_train, y_test) = keras.datasets.mnist.load_data()

#normal 0-1 range
x_train = x_train / 255.0
x_test = x_test / 255.0

#Visualize some digits
plt.figure(figsize=(6, 6))
for i in range(9):
  plt.subplots(3, 3, i + 1)
  plt.imshow(x_train[i], cmap='gray')
  plt.title(f'Label: {y_train[i]}')
  plt.axis('off')
plt.show()