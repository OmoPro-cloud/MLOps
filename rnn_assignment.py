import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers


url = "https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv"
df = pd.read_csv(url)
print(df.head())

plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Closing Price')
plt.title('Stock Price Over Time')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()

#pre-process the data - in this section we use the lstm to predict the next closing price
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

#How many days to look at
lookback_days = 30
x, y = [], []

for i in range(lookback_days, len(scaled_data)):
  x.append(scaled_data[i - lookback_days:i, 0])
  y.append(scaled_data[i, 0])

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1)) #LSTM expects 3D input
#Split the data into train and test
train_size = int(len(x) * 0.8)
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

#build the LSTM model
model = keras.Sequential([
  layers.GRU(100, return_sequences=True, input_shape=(x_train.shape[-1], 1)), 
  layers.GRU(100, return_sequences=False), #GATED RECURRING UNIT
  layers.Dense(25),
  layers.Dense(1)
])
model.compile(optimizer='RMSProp', loss='means_squared_error')

#Evaluate and predict
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

#Visualize the prediction
plt.figure(figsize=(10, 6))
plt.plot(y_test_actual, label='Actual Price')
plt.plot(predictions, label='Predicted Price')
plt.title('Stock Price Prediction')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()