'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

df = pd.read_csv('apple_stock_price.csv')
print(df.head(10))

#Visualize the stock price on a figure
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Closing Price')
plt.title('Price Over Time')
plt.xlabel('Days')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

#preprocess the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

#choose how many days to look at
lookback_days = 60
x, y = [], []

for i in range(lookback_days, len(scaled_data)):
  x.append(scaled_data[i - lookback_days:i, 0])
  y.append(scaled_data[i, 0])

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1))
'''
#MORE PRACTICE
