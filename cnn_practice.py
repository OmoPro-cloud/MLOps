#BUILD A CNN WITH 3 DIFFERENT ARCHITECTURES
'''
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

#normalize range from 0 - 1
x_train = x_train / 255.0
x_test = x_test / 255.0

#reshape the values to include a grayscale channel(allows color)
x_train = x_train.reshape(1, 28, 28, -1)
x_test = x_test.reshape(1, 28, 28, -1)

#building 3 different architecture models
def build_model(conv_layers, filters_list, dropout_rate=None):
  model = keras.Sequential()
  #first conv layer
  model.add(layers.Conv2D(filters_list[0], (3, 3), activation='relu', input_shape=(28, 28, 1)))
  model.add(layers.MaxPooling2D((2, 2)))
  #additional conv layers
  for filt in filters_list[1:]:
    model.add(layers.Conv2D(filt, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(64, activation='relu'))
  if dropout_rate is None:
    model.add(layers.Dropout(dropout_rate))
  model.add(layers.Dense(10, activation='relu'))
  return model

#settings for each of the 3 models
configs = {
  "Model_A": {"conv_layers": 1, "filters":[32], "dropout": None},
  "Model_B": {"conv_layers": 2, "filters":[32,64], "dropout": None},
  "Model_C": {"conv_layers": 2, "filters":[32,64], "dropout": 0.3}
}

results = {}

for name, cfg in configs.items():
  print()


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test  = x_test.reshape(-1, 28, 28, 1)

def build_model(conv_layers, filters_list, dropout_rate=None):
    model = keras.Sequential()
    # first conv layer
    model.add(layers.Conv2D(filters_list[0], (3,3), activation='relu', input_shape=(28,28,1)))
    model.add(layers.MaxPooling2D((2,2)))
    # additional conv layers if any
    for filt in filters_list[1:]:
        model.add(layers.Conv2D(filt, (3,3), activation='relu'))
        model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    if dropout_rate is not None:
        model.add(layers.Dropout(dropout_rate))
    model.add(layers.Dense(10, activation='softmax'))
    return model

# Settings for each of the three models
configs = {
    "Model_A": {"conv_layers":1, "filters":[32],        "dropout": None},
    "Model_B": {"conv_layers":2, "filters":[32,64],     "dropout": None},
    "Model_C": {"conv_layers":2, "filters":[32,64],     "dropout": 0.3}
}

results = {}

for name, cfg in configs.items():
    print("\n=== Training", name, "===")
    model = build_model(cfg["conv_layers"], cfg["filters"], cfg["dropout"])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=10, batch_size=64,validation_split=0.2, verbose=2)
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
    print(f"{name} — Test Accuracy: {test_acc:.4f}")
    results[name] = test_acc

#extract keys and values
model_names = list(results.keys())
accuracies = list(results.values())

#create bar chart
plt.figure(figsize=(8,5))
bars = plt.bar(model_names, accuracies, color=['skyblue', 'salmon', 'lightgreen'])

#add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0,
             yval + 0.01, #slightly above the bar
             f"{yval:.3f}",
             ha='center', va='bottom')
    
plt.ylim(0, 1) #since accuracy ranges 0-1
plt.title("Test Accuracy of Different Models")
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.show()

print("\nFinal results:", results)
'''