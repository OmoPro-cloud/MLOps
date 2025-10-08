'''NEURAL NETWORKS ARE CAPABLE OF LEARNING INCREDIBLY COMPLEX OR NON-LINEAR MODELS
TENSORFLOW IS A POPULAR FRAMEWORK FOR CREATING THE MODEL
A NEURAL NETWORK IS CONNECTED BY NEURONS'''

#Multi Layer Perceptrons
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

#Load the dataset
#MNIST dataset of handwritten digits. It is built into keras
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#Normalize 0-1 range
x_train = x_train / 255.0
x_test = x_test /255.0

#Visualize some digits
plt.figure(figsize=(6, 6))
for i in range(9):
  plt.subplot(3, 3, i + 1)
  plt.imshow(x_train[i], cmap='gray')
  plt.title(f"Label: {y_train[i]}")
  plt.axis('off')
plt.show()


#we are building a multilayered perceptron
#the way a neural network learns is through back propagation
#a high learning rate is fast but risky, a low learning rate is slow but more reliable
#contains 70,000 images of handwritten digits from 0-9

#Flatten and build the model
model = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)), #Flatten the 20x28 images into 784-element vectors
  layers.Dense(128, activation='relu'), #Hidden layer with 128 neurons and ReLu activation(Rectified Linear Unit)
  layers.Dense(64, activation='relu'),
  layers.Dense(10, activation='softmax') #Output layer with 10 (one per class) and softmax activated
])

#Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

#Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest accuracy: {test_acc:.3f}")

#Visualize the training performance
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()