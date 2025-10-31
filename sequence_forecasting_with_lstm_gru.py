import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers
import time
from sklearn.metrics import mean_squared_error

# Load dataset
url = "https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv"
data = pd.read_csv(url)
print(data.head())

# Visualize the stock price
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Closing Price')
plt.title('Stock Price Over Time')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()

# Preprocess the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

# Create sequences for training
lookback_days = 90
x, y = [], []
for i in range(lookback_days, len(scaled_data)):
    x.append(scaled_data[i - lookback_days:i, 0])
    y.append(scaled_data[i, 0])

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1))

# Split the data
train_size = int(len(x) * 0.8)
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

#lstm model
lstm_model = keras.Sequential([
    layers.LSTM(1000, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    layers.LSTM(1000, return_sequences=False),
    layers.Dense(25),
    layers.Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mean_squared_error')

start_time = time.time()
lstm_model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1)
lstm_time = time.time() - start_time

# Predict with LSTM
lstm_predictions = lstm_model.predict(x_test)
lstm_predictions = scaler.inverse_transform(lstm_predictions)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

#gru model
gru_model = keras.Sequential([
    layers.GRU(1000, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    layers.GRU(1000, return_sequences=False),
    layers.Dense(25),
    layers.Dense(1)
])
gru_model.compile(optimizer='adam', loss='mean_squared_error')

start_time = time.time()
gru_model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1)
gru_time = time.time() - start_time

# Predict with GRU
gru_predictions = gru_model.predict(x_test)
gru_predictions = scaler.inverse_transform(gru_predictions)

#visualization
plt.figure(figsize=(12, 6))
plt.plot(y_test_actual, label='Actual Price', color='black')
plt.plot(lstm_predictions, label='LSTM Predicted Price', color='blue')
plt.plot(gru_predictions, label='GRU Predicted Price', color='red')
plt.title('Stock Price Prediction: LSTM vs GRU')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()

#comparison


lstm_mse = mean_squared_error(y_test_actual, lstm_predictions)
gru_mse = mean_squared_error(y_test_actual, gru_predictions)

print(f"LSTM MSE: {lstm_mse:.6f}")
print(f"GRU  MSE: {gru_mse:.6f}")
print(f"LSTM Training Time: {lstm_time:.2f} seconds")
print(f"GRU  Training Time: {gru_time:.2f} seconds")
