#RNN - Recurrent Nueral Network
#LSTM - Long Short Term Memory
#Neural Machine Translation - uses deep learning to learn the mapping between languages. This method processes entire sentences or even paragraphs rather than word by word phrases

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers

url = "https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv"
data = pd.read_csv(url)
print(data.head())

#visualize the stock price on a figure
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Closing Price')
plt.title('Stock Price Over Time')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()

#pre-process the data - in this section we use the lstm to predict the next closing price
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

#How many days to look at
lookback_days = 60
x, y = [], []

for i in range(lookback_days, len(scaled_data)):
  x.append(scaled_data[i - lookback_days:i, 0])
  y.append(scaled_data[i, 0])

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1)) #LSTM expects 3D input
