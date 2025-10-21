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

print("\nFinal results:", results)