import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()
# Value x & y
x = iris.data
y = iris.target
# iris.feature
print(iris.feature_names)

# Make graph
plt.scatter(x[:,2], x[:,3], c=y)
# label
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
# Title Iris Dataset
plt.title("IRIS DATASET")
plt.show()