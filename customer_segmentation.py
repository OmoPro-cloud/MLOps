import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('customers.csv')
#print(df).head()

#Select features for clustering
X = df.read[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
#
'''
We want to segment our customers
-e.g. Are they young?
- which products do they like the most/least?
- what is their annual income?
- do  people spend more? and on what?
'''

#Scale the data
scaler = StandardScaler()