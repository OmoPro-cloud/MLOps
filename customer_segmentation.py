import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('customers.csv')
#print(df).head()

#Select features for clustering
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
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
X_scaled = scaler.fit_transform(X)

#Fit KMeans Model
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print(df.groupby('Cluster').mean())
#we use groupby to calculate the average age, average income and average spending score of the customers