df.head()

x=df.iloc[:, [2, 3]].values

x.shape

from sklearn.cluster import DBSCAN
db=DBSCAN(eps=3, min_samples=4, metric='euclidean')

model=db.fit(x)

label=model.labels_

label

from sklearn import metrics

sample_cores=np.zeros_like(label, dtype=bool)

sample_cores[db.core_sample_indices_] = True

n_clusters = len(set(label)) - (1 if -1 in label else 0)
print('No of clusters:', n_clusters)

y_means = db.fit_predict(x)
plt.figure(figsize=(7,5))
colors = ['pink', 'yellow', 'cyan', 'magenta', 'orange', 'blue', 'red', 'black', 'violet']
for i in range(min(len(colors), n_clusters)):
    plt.scatter(x[y_means == i, 0], x[y_means == i, 1], s = 50, c = colors[i], label=f'Cluster {i}')

plt.xlabel('Annual Income in (k)')
plt.ylabel('Spending Score from 1-100')
plt.title('Clusters of data (DBSCAN)')
plt.legend()
plt.show()

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(x, method = 'ward'))
plt.title('Dendrogram', fontsize = 20)
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()

from sklearn.cluster import AgglomerativeClustering
# Changed 'affinity' to 'metric' to fix the TypeError
hc = AgglomerativeClustering(n_clusters = 9, metric = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(x)

plt.figure(figsize=(7,5))
for i in range(9):
    plt.scatter(x[y_hc == i, 0], x[y_hc == i, 1], s = 50, c = colors[i], label=f'Cluster {i}')

plt.title('Hierarchical clustering', fontsize = 20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.grid()
plt.show()