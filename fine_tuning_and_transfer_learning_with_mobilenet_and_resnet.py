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
model_mobilenet = build_model(base_mobilenet)
model_resnet = build_model(base_resnet)

#Compile both
model_mobilenet.compile(optimizer='adam',
                        loss='binary_crossentropy',
                        metrics=['accuracy'])
model_resnet.compile(optimizer='adam',
                     loss='binary_crossentropy',
                     metrics=['accuracy'])

#Train both
print('Training MobileNetV2 model')
history_mobilenet = model_mobilenet.fit(
  train_data,
  epochs=5,
  validation_data=val_data
)

print('ResNet50 Training model')
history_resnet = model_resnet.fit(
  train_data,
  epochs=5,
  validation_data=val_data
)

#Fine tuning: unfreezing the top layers of each
for m, base in [(model_mobilenet, base_mobilenet), (model_resnet, base_resnet)]:
  base.trainable = True
  #freeze all but the last 30 layers
  for layer in base.layers[:-30]:
    layer.trainable = False
  m.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
            loss='binary_crossentropy',
            metrics=['accuracy'])
  print('Fine Tuning Model: ', base.name)
  _ = m.fit(train_data,
            epochs=5,
            validation_data=val_data)
  
#Evaluate
acc_mn = model_mobilenet.evaluate(val_data)
acc_rn = model_resnet.evaluate(val_data)
print(f"MobileNetV2 Validation Accuracy: {acc_mn[1]*100:.2f}%")
print(f"ResNet50 Validation Accuracy: {acc_rn[1]*100:.2f}%")

# Plot both accuracy curves
plt.figure(figsize=(10,5))
plt.plot(history_mobilenet.history['accuracy'] + history_mobilenet.history.get('val_accuracy', []),
         label='MobileNetV2 – train')
plt.plot(history_mobilenet.history.get('val_accuracy', []),
         label='MobileNetV2 – val')
plt.plot(history_resnet.history['accuracy'] + history_resnet.history.get('val_accuracy', []),
         label='ResNet50 – train')
plt.plot(history_resnet.history.get('val_accuracy', []),
         label='ResNet50 – val')
plt.title('Training & Validation Accuracy for Two Models')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()