'''
TRANSFER LEARNING AND FINE-TUNING(used in Deep Learning)

in short, transfer learning consists of taking features that have been used on one model and using it on another model(e.g. some features from a model that was used to identify raccoons can be leveraged in a new model to identify corgis)

common steps of transfer learning in the context of deep learning:
1. Take layers from a previously trained model
2. Freeze them, so they do not destroy any of the information they contain during future training rounds
3. Add new, trainable layers on top of the frozen layers. They will learn to turn the old features into predictions on a dataset
4. Train the new layers on your dataset

The last step is fine-tuning, although this is optional. This consists of unfreezing all the transferred features and training them on a very low learning rate. This can potentially achieve meaningful improvements, by incrementally adapting the pretrained features to the new data.


'''

import numpy as np
import keras
from keras import layers
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

'''
FREEZING LAYERS

Layers & models have three weight attributes:
- Weights is the list of all weights variables of the layer.
- Trainable_weights is the list of those that are meant to be updated (via gradient descent) to minimize the loss during training.
- non_trainable_weights is the list of those that aren't meant to be trained. Typically they are updated by the model during the forward pass.

Layers & models also feature a boolean attribute. Its value can be changed. Setting "layer.trainable" to "False" moves all the layer's weights from trainable to non-trainable. This is called "freezing" the layer: the state of a frozen layer won't be updated during training

In general, all weights are trainable weights. The only built-in layer that has non-trainable weights is the BatchNormalization layer. When a trainable weight becomes non trainable, its value is no longer updated during trainaing.
'''

layer = keras.layers.Dense(3)
#layer2 = keras.layers.BatchNormalization() <-- example using a BatchNormalization layer 
layer.build((None, 4)) #Create the weight

print('weights: ', len(layer.weights))
print('trainable weights: ', len(layer.trainable_weights))
print('non-trainable weights: ', len(len.non_trainable_weights))

'''
RECURSIVE SETTING OF THE TRAINABLE ATTRIBUTE

If you set trainable = False on a model or on any layer that has sublayers, all children layers become non-trainable as well.

e.g. inner_model = keras.Sequential(
    [
        keras.Input(shape=(3,)),
        keras.layers.Dense(3, activation="relu"),
        keras.layers.Dense(3, activation="relu"),
    ]
)

model = keras.Sequential(
    [
        keras.Input(shape=(3,)),
        inner_model,
        keras.layers.Dense(3, activation="sigmoid"),
    ]
)

model.trainable = False  # Freeze the outer model

assert inner_model.trainable == False  # All layers in `model` are now frozen
assert inner_model.layers[0].trainable == False  # `trainable` is propagated recursively

TYPICAL TRANSFER LEARNING WORKFLOW

there are two common workflows, a normal one and a lightweight workflow:

1. Instantiate a base model and load pre-trained weights into it.
2. Freeze all layers in the base model by setting trainable = False.
3. Create a new model on top of the output of one (or several) layers from the base model.
4. Train your new model on your new dataset.

Lightweight workflow:
1. Instantiate a base model and load pre-trained weights into it.
2. Run your new dataset through it and record the output of one (or several) layers from the base model. This is called FEATURE EXTRACTION.
3. Use that output as input data for a new, smaller model.

PROS & CONS OF THE SECOND WORKFLOW:

Pros:
- you only run the base model once on your data, instead of once per epoch of training, therefore it is a lot faster and cheaper

Cons:
- the second workflow, however does not allow you to dynamically modify the input data of your new model during training, which is essential when doing data augmentation. transfer learning is typically used when your new dataset has too little data to train a full-scale model from scratch and in these scenarios, data augmentation is CRUCIAL. Therfore, we will usually follow the first workflow.
'''

#Here's what the first Transfer Learning Worklow looks like:
base_model = keras.applications.Xception( #first you instantiate a model with pre-trained weights
    weights='imagenet',  # Load weights pre-trained on ImageNet.
    input_shape=(150, 150, 3),
    include_top=False)  # Do not include the ImageNet classifier at the top.

#Then, freeze the base model.
base_model.trainable = False

#Now, create a new model on top
inputs = keras.Input(shape=(150, 150, 3))
x = base_model(inputs, training=False) #We make sure that the base_model is running in inference mode here, by passing `training=False`. This is important for fine-tuning
x = keras.layers.GlobalAveragePooling2D()(x)#Convert features of shape to vectors
outputs = keras.layers.Dense(1)(x)#a Dense classifier with a single unit(binary classification)
model = keras.Model(inputs, outputs)

#Train the model on new data
model.compile(optimizer=keras.optimizers.Adam(),
              loss=keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[keras.metrics.BinaryAccuracy()])
model.fit(new_dataset, epochs=5, callbacks=..., validation_data=...)#set epochs to 20

'''
FINE-TUNING

Once your model has converged on the new data, you can try to unfreeze all or part of the base model and retrain the whole model end-to-end with a very low learning rate.

This is an optional last step that can potentially give you incremental improvements. It COULD ALSO POTENTIALLY LEAD TO OVERFITTING – keep that in mind.

It is critical to ONLY DO THIS STEP AFTER THE MODEL WITH THE FROZEN LAYERS HASA BEEN TRAINED TO CONVERGENCE. If you mix randomly-initialized trainable layers with trainable layers that hold pre-trained features, the randomly-initialized layers will cause very large gradient updates during training, which will destroy your pre-trained features.

It's also critical to use a very low learning rate at this stage, because you are training a much larger model than in the first round of training, on a dataset that is typically very small. As a result, you are at risk of overfitting very quickly if you apply large weight updates. Here, you only want to readapt the pretrained weights in an incremental way
'''

# Unfreeze the base model
base_model.trainable = True

#It's important to recompile your model after you make any changes to the `trainable` attribute of any inner layer, so that your changes are take into account
model.compile(optimizer=keras.optimizers.Adam(1e-5),  # Very low learning rate
              loss=keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[keras.metrics.BinaryAccuracy()])

# Train end-to-end. Be careful to stop before you overfit!
model.fit(new_dataset, epochs=10, callbacks=..., validation_data=...)

'''
Important notes about compile() and trainable

Calling compile() on a model is meant to "freeze" the behavior of that model. This implies that the trainable attribute values at the time the model is compiled should be preserved throughout the lifetime of that model, until compile is called again. Hence, if you change any trainable value, make sure to call compile() again on your model for your changes to be taken into account.
'''





'''
Fine-Tuning an image classification model on a cats vs. dogs dataset

END TO END TRANSFER LEARNING AND FINE-TUNING EXAMPLE

Transfer learning is most useful when working with very small datasets. To keep our dataset small, we will use 40% of the original training data (25,000 images) for training, 10% for validation, and 10% for testing.
'''

tfds.disable_progress_bar()

train_ds, validation_ds, test_ds = tfds.load(
    "cats_vs_dogs",
    # Reserve 10% for validation and 10% for test
    split=["train[:40%]", "train[40%:50%]", "train[50%:60%]"],
    as_supervised=True,  # Include labels
)

print(f"Number of training samples: {train_ds.cardinality()}")
print(f"Number of validation samples: {validation_ds.cardinality()}")
print(f"Number of test samples: {test_ds.cardinality()}")

#show images
plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(int(label))
    plt.axis("off")

#label '1' is for dogs, label '0' is for cats

'''
STANDARDIZING THE DATA


'''