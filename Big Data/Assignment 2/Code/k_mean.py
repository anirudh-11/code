import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5)

dataset = pd.read_csv('Mall_Customers.csv')
dataset.plot.scatter(x='Annual Income (k$)', y = 'Spending Score (1-100)')
plt.show()
sns.lmplot(x='Annual Income (k$)', y = 'Spending Score (1-100)', hue = 'Genre', data=dataset)
plt.show()
X = dataset.iloc[:, [3,4]].values

y_mean = kmeans.fit_predict(X)

plt.figure(figsize=(20,10))
plt.figure(1 , figsize = (17 , 8))
plt.scatter(X[y_mean == 0, 0], X[y_mean == 0, 1], s = 10, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_mean == 0, 0], X[y_mean == 0, 1], s = 10, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_mean == 1, 0], X[y_mean == 1, 1], s = 10, c = 'yellow', label = 'Cluster 2')
plt.scatter(X[y_mean == 2, 0], X[y_mean == 2, 1], s = 10, c = 'aqua', label = 'Cluster 3')
plt.scatter(X[y_mean == 3, 0], X[y_mean == 3, 1], s = 10, c = 'violet', label = 'Cluster 4')
plt.scatter(X[y_mean == 4, 0], X[y_mean == 4, 1], s = 10, c = 'lightgreen', label = 'Cluster 5')
plt.title('Clustering based on Annual income v/s Spending Score')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 30, c = 'navy', label = 'Centroids')
plt.legend()
plt.show()