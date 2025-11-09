import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

train_datagen = ImageDataGenerator(
  rescale=1./255,
  
)