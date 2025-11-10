'''
import tensorflow as tf #the main ML framework
from tensorflow.keras import layers, models #this lets us build neural network architectures
from tensorflow.keras.preprocessing.image import ImageDataGenerator #used for image augmentation/preprocessing
import matplotlib.pyplot as plt
import numpy as np

train_datagen = ImageDataGenerator(
  rescale=1./255, #scales all image pixel values by 1/255, helping the neural network train more stably
  rotation_range=20, #the images are randomly rotated, between -20 and +20 degrees each time they are turned into a batch, making model more robust
  zoom_range=0.2, #random zooming in the range of 0.2 will be applied to images
  horizontal_flip=True #Each image may be flipped left or right horizontally. Good for augmenting data if horizontal orientation doesn’t matter in your domain.
)

val_data = ImageDataGenerator(1./255)

train_data = train_datagen.flow_from_directory(
  'chest_xray/train',
  target_size=(128, 128), #every image will be resized up to 128 pixels before being passed to the model
  batch_size=32, #the generator will yield batches of 32 images and their labels at the time
  class_mode='binary'
)

#Load MobileNetV2 <-- the pretrained model we are fine tuning

base_model = tf.keras.applications.MobileNetV2(input_shape=(128, 128, 3),
                                               include_top=False,
                                               weights='imagenet')

base_model.trainable = False

#Add a custom classification head
model = models.Sequential([
  base_model,
  layers.GlobalAveragePooling2D(),
  layers.Dense(128, activation='relu'),
  layers.Dropout(0.3),
  layers.Dense(1, activation='sigmoid')
])

#Compile the model

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
  train_data,
  epochs=5,
  validation_data = val_data
)

#After training, fine tune the top layers
base_model.trainable = True
for layer in base_model.layers[:-30]:
  layer.trainable = False

model.compile(optimizer=tf.keras.optimizers(1e-5),
              loss='binary_crossentropy',
              metrics=['accuracy'])

fine_tune_history = model.fit(
  train_data,
  epochs = 5,
  validation_data = val_data
)

#Evaluate and Visualize
acc = model.evacuate(val_data)
print(f"Validation Accuracy: {acc[1]*100:.2f}")

plt.plot(history.history['accuracy'] + fine_tune_history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()
'''

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

train_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=20,
  zoom_range=0.2,
  horizontal_flip=True
)

val_data = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
  'chest_xray/train',
  target_size=(128, 128), #we resize our images to match the exact size the MobileNet was trained on, THIS IS CRITICAL
  batch_size=32,
  class_mode='binary'

)

val_data = val_data.flow_from_directory(
  'chest_xray/test',
  target_size=(128, 128), #224
  batch_size=32,
  class_mode='binary'
)

#Load the pre trained model MobileNetV2

base_model = tf.keras.applications.MobileNetV2(input_shape=(128, 128, 3),
                                            include_top=False, #Dont include imagenet classifier
                                            weights='imagenet')

base_model.trainable = False #Freeze the base model(feature extraction)

#Add a custom classification head
model = models.Sequential([
  base_model,
  layers.GlobalAveragePooling2D(),
  layers.Dense(128, activation='relu'),
  layers.Dropout(0.3),
  layers.Dense(1, activation='sigmoid')
])

#Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
  train_data,
  epochs=5,
  validation_data = val_data
)

#After training, fine tune the top layers
base_model.trainable = True
for layer in base_model.layers[:-30]:
  layer.trainable = False
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), #1e-5 makes the model learn slower
              loss='binary_crossentropy',
              metrics=['accuracy'])
fine_tune_history = model.fit(
  train_data,
  epochs=5,
  validation_data=val_data
)

#Evaluate and Visualize
acc = model.evaluate(val_data)
print(f"Validation Accuracy: {acc[1]*100:.2f}")

plt.plot(history.history['accuracy'] + fine_tune_history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()