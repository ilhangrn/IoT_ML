# https://scikit-learn.org/stable/auto_examples/datasets/plot_random_dataset.html
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html

print(__doc__)

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import make_gaussian_quantiles

plt.figure(figsize=(15, 15))
plt.subplots_adjust(bottom=.05, top=.9, left=.05, right=.95)

rs = 100 # 150
plt.subplot(321) # 3 rows, 2 columns
plt.title("One informative feature, one cluster per class", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1,
                             n_clusters_per_class=1, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1, # color coded as Y1
            s=25, edgecolor='k')

plt.subplot(322)
plt.title("Two informative features, one cluster per class", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2,
                             n_clusters_per_class=1, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(323)
plt.title("Two informative features, two clusters per class",
          fontsize='small')
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=rs)
plt.scatter(X2[:, 0], X2[:, 1], marker='o', c=Y2,
            s=25, edgecolor='k')

plt.subplot(324)
plt.title("Multi-class, two informative features, one cluster",
          fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2,
                             n_clusters_per_class=1, n_classes=3, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(325)
plt.title("Three blobs", fontsize='small')
X1, Y1 = make_blobs(n_features=2, centers=3, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(326)
plt.title("Gaussian divided into three quantiles", fontsize='small')
X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.show()


# Different noise levels, etc.
# flip_y, The fraction of samples whose class is assigned randomly.
# default: 0.01

plt.figure(figsize=(8, 8))
plt.subplots_adjust(bottom=.05, top=.9, left=.05, right=.95)

plt.subplot(221)
plt.title("One informative feature, one cluster per class, one redundant", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=1, n_informative=1,
                             n_clusters_per_class=1, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(222)
plt.title("One informative feature, one cluster per class, flip 0.2", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1,
                             n_clusters_per_class=1, flip_y = 0.2, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(223)
plt.title("Two informative features, one cluster per class, flip 0.2", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2,
                             n_clusters_per_class=1, flip_y = 0.2, random_state=rs)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1,
            s=25, edgecolor='k')

plt.subplot(224)
plt.title("Two informative features, two clusters per class, flip 0.2",
          fontsize='small')
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2, flip_y = 0.2, random_state=rs)
plt.scatter(X2[:, 0], X2[:, 1], marker='o', c=Y2,
            s=25, edgecolor='k')
plt.show()