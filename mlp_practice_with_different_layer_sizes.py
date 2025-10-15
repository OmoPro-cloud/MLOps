import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers 
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

plt.figure(figsize=(6, 6))
for i in range(9):
  plt.subplot(3, 3, i + 1)
  plt.imshow(x_train[i], cmap='gray')
  plt.title(f"Label: {y_train[i]}")
  plt.axis('off')
  plt.show()

firstModel = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(128, activation='relu'),
  layers.Dense(64, activation='relu'),
  layers.Dense(10, activation='softmax')
])

secondModel = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(64, activation='relu'),
  layers.Dense(32, activation='relu'),
  layers.Dense(10, activation='softmax')
])

thirdModel = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(256, activation='relu'),
  layers.Dense(128, activation='relu'),
  layers.Dense(10, activation='softmax')
])

firstModel.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])
firstHistory = firstModel.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

secondModel.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])
secondHistory = secondModel.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

thirdModel.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])
thirdHistory = thirdModel.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

test_loss, test_acc = firstModel.evaluate(x_test, y_test, verbose=2)
print(f"\nFirst Model Test Accuracy: {test_acc:.3f}")

test_loss, test_acc = secondModel.evaluate(x_test, y_test, verbose=2)
print(f"\nSecond Model Test Accuracy: {test_acc:.3f}")

test_loss, test_acc = thirdModel.evaluate(x_test, y_test, verbose=2)
print(f"\nThird Model Test Accuracy: {test_acc:.3f}")

plt.plot(firstHistory.history['accuracy'], label='Training Accuracy')
plt.plot(firstHistory.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(secondHistory.history['accuracy'], label='Training Accuracy')
plt.plot(secondHistory.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(thirdHistory.history['accuracy'], label='Training Accuracy')
plt.plot(thirdHistory.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()