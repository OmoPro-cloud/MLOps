import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

def build_model(hidden_units=[128, 64], learning_rate=1e-3):
    model = keras.Sequential()
    model.add(layers.Input(shape=(28,28)))
    model.add(layers.Flatten())
    for u in hidden_units:
        model.add(layers.Dense(u, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

def load_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    # normalize
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    # one‑hot labels
    num_classes = 10
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return x_train, y_train, x_test, y_test

def plot_history(history, title_suffix=""):
    plt.figure(figsize=(12,5))
    # accuracy
    plt.subplot(1,2,1)
    plt.plot(history.history['accuracy'], label='train acc')
    if 'val_accuracy' in history.history:
        plt.plot(history.history['val_accuracy'], label='val acc')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy ' + title_suffix)
    plt.legend()
    # loss
    plt.subplot(1,2,2)
    plt.plot(history.history['loss'], label='train loss')
    if 'val_loss' in history.history:
        plt.plot(history.history['val_loss'], label='val loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss ' + title_suffix)
    plt.legend()
    plt.show()

def experiment(hidden_units=[128,64], learning_rate=1e-3, batch_size=64, epochs=20):
    x_train, y_train, x_test, y_test = load_data()
    # further split some validation
    # e.g. use validation_split in fit
    model = build_model(hidden_units, learning_rate)
    history = model.fit(
        x_train, y_train,
        validation_split=0.1,
        epochs=epochs,
        batch_size=batch_size,
        verbose=2
    )
    # evaluate
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", test_loss, "Test accuracy:", test_acc)
    plot_history(history, f"hu={hidden_units}, lr={learning_rate}, bs={batch_size}")
    # save
    model.save("digit_mlp.h5")
    return model, history, (test_loss, test_acc)

def reload_and_test():
    from tensorflow.keras.models import load_model
    model2 = load_model("digit_mlp.h5")
    x_train, y_train, x_test, y_test = load_data()
    test_loss, test_acc = model2.evaluate(x_test, y_test, verbose=0)
    print("Reloaded model test accuracy:", test_acc, "loss:", test_loss)
    return model2

if __name__ == '__main__':
    # example run
    model, history, (loss, acc) = experiment(
        hidden_units=[128, 64], learning_rate=1e-3, batch_size=64, epochs=15
    )
    model2 = reload_and_test()