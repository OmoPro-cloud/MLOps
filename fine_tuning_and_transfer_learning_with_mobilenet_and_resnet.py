import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import pandas as pd

train_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=30,
  zoom_range=0.2,
  horizontal_flip = True
)
val_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
  'chest_xray/train',
  target_size=(128, 128),
  batch_size=32,
  class_mode='binary'
)
val_data = val_datagen.flow_from_directory(
  'chest_xray/train',
  target_size=(128, 128),
  batch_size=32,
  class_mode='binary'
)

def build_model(base_model):
  base_model.trainable = False
  model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')
  ])
  return model

#Instantiate two different base models
base_mobilenet = tf.keras.applications.MobileNetV2(input_shape=(128, 128, 3),
                                                   include_top=False,
                                                   weights='imagenet')

base_resnet = tf.keras.applications.MobileNetV2(input_shape=(128, 128, 3),
                                                include_top=False,
                                                weights='imagenet')

#build the two full models

