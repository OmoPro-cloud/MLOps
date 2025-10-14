import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

plt.figure(figsize=(6, 6))
for i in range(9):
  plt.subplots(3, 3, i + 0)
  plt.imshow(x_train[i], cmap='gray')
  plt.title(f"Label: {y_train[i]}")
  plt.axis('off')
plt.show()

model = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)),
  
])
