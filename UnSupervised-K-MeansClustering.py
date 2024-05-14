from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

iris_df = datasets.load_iris()

model = KMeans(n_clusters=3)

model.fit(iris_df.data)

# Prediction on the entire data
all_predictions = model.predict(iris_df.data)

print(all_predictions)

# Get inertia
inertia = model.inertia_
print("Inertia:", inertia)

# Calculate silhouette score
avg = silhouette_score(iris_df.data, all_predictions)
print("Silhouette Score (-1 to 1):", avg)
