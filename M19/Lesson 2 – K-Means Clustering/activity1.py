import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly as py
import plotly.graph_objs as go

from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

from google.colab import files
file = files.upload()
# Using the first key in the uploaded files dict to handle duplicate uploads automatically
filename = list(file.keys())[0]
df = pd.read_csv(filename, index_col=0)

plt.figure(1, figsize = (15 , 6))
n = 0
for x in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.distplot(df[x] , bins = 15)
    plt.title('Distplot of {}'.format(x))
plt.show()

sns.pairplot(df, vars = ['Spending Score (1-100)', 'Annual Income (k$)', 'Age'], hue = "Gender")

plt.figure(1, figsize = (15 , 7))
plt.title('Scatter plot of Age v/s Spending Score', fontsize = 20)
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.scatter(x = 'Age', y = 'Spending Score (1-100)', data = df, s = 100)
plt.show()

x1 = df[['Age', 'Spending Score (1-100)']].values
inertia = []
for n in range(1, 15):
    algorithm = (KMeans(n_clusters = n, init='k-means++', n_init = 10, max_iter=300,
    tol=0.0001, random_state=111, algorithm='elkan'))
    algorithm.fit(x1)
    inertia.append(algorithm.inertia_)

plt.figure(1, figsize = (15,6))
plt.plot(np.arange(1, 15), inertia, 'o')
plt.plot(np.arange(1, 15), inertia, '-', alpha = 0.5)
plt.xlabel('Number of Clusters'), plt.ylabel('Inertia')
plt.show()

algorithm = (KMeans(n_clusters = 4, init='k-means++', n_init = 10, max_iter=300, tol=0.0001, random_state=111, algorithm='elkan'))
algorithm.fit(x1)
labels1 = algorithm.labels_
centroids1 = algorithm.cluster_centers_

h = 0.02
x_min, x_max = x1[:, 0].min() - 1, x1[:, 0].max() + 1
y_min, y_max = x1[:, 1].min() - 1, x1[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = algorithm.predict(np.c_[xx.ravel(), yy.ravel()])

plt.figure(1, figsize=(15, 7))
z = Z.reshape(xx.shape)
plt.imshow(z, interpolation='nearest',
extent=(xx.min(), xx.max(), yy.min(), yy.max()),
cmap = plt.cm.Pastel2, aspect = 'auto', origin='lower')

plt.scatter(x = 'Age', y = 'Spending Score (1-100)', data = df, c = labels1, s = 100)
plt.scatter(x = centroids1[:, 0], y = centroids1[:, 1], s = 300, c = 'red', alpha = 0.5)
plt.ylabel('Spending Score (1-100)')
plt.show()

x2 = df[['Annual Income (k$)', 'Spending Score (1-100)']].values
inertia = []
for n in range(1, 11):
    algorithm = (KMeans(n_clusters = n, init='k-means++', n_init = 10, max_iter=300,
    tol=0.0001, random_state=111, algorithm='elkan'))
    algorithm.fit(x2)
    inertia.append(algorithm.inertia_)

algorithm = (KMeans(n_clusters = 5, init='k-means++', n_init = 10, max_iter=300,
tol=0.0001, random_state=111, algorithm='elkan'))
algorithm.fit(x2)
labels2 = algorithm.labels_
centroids2 = algorithm.cluster_centers_

X3 = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].values
algorithm = (KMeans(n_clusters = 6, init='k-means++', n_init = 10, max_iter=300,
tol=0.0001, random_state=111, algorithm='elkan'))
algorithm.fit(X3)
# Assigning labels directly to avoid index mismatch errors
df['cluster'] = algorithm.labels_

trace1 = go.Scatter3d(
    x= df['Age'],
    y= df['Spending Score (1-100)'],
    z= df['Annual Income (k$)'],
    mode='markers',
    marker=dict(
        color= df['cluster'],
        size= 10,
        line=dict(
            color= df['cluster'],
            width= 12
        ),
        opacity=0.8
    )
)

data = [trace1]
layout = go.Layout(
    title= 'Clusters wrt Age, Income and Spending Scores',
    scene= dict(
        xaxis= dict(title= 'Age'),
        yaxis= dict(title= 'Spending Score'),
        zaxis= dict(title= 'Annual Income')
    )
)
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig)

display(df.head())