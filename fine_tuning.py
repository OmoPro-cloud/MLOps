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

val_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
  'chest_xray/train',
  target_size=(224, 224), #we resize our images to match the size the MobileNet was trained on, THIS IS CRITICAL
  batch_size=32,
  class_mode='binary'

)

val_datagen = val_datagen.flow_from_directory(
  'chest_xray/test',
  target_size=(224, 224),
  batch_size=32,
  class_mode='binary'
)

#Load the pre trained model MobileNetV2

base_model = keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                            include_top=False, #Dont include imagenet classifier
                                            weights='imagenet')

base_model.trainable = False #Freeze the base model(feature extraction)

#Add a custom classification head
model = models.Sequential([
  base_model,
  layers.GlobalAveragePooling2D(),
  layers.Dense(128, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(0.3),
  layers.Dense(1, activation='sigmoid')
])

#Compile the model
model.compile(optimizer='adam',
              loss='binary_croseentropy',
              metrics=['accuracy'])

history = model.fit(
  train_data,
  epochs=5,
  validation_data = val_datagen
)