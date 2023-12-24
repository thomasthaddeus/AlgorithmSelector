import numpy as np
import random

class KMeans:
    def __init__(self, k=2, max_iterations=100):
        self.k = k  # Number of clusters
        self.max_iterations = max_iterations  # Maximum number of iterations

    def initialize_centroids(self, data):
        """Randomly initialize the centroids using the data points."""
        indices = random.sample(range(len(data)), self.k)
        centroids = [data[idx] for idx in indices]
        return centroids

    def assign_clusters(self, data, centroids):
        """Assign data points to the nearest centroid."""
        clusters = [[] for _ in range(self.k)]
        for point in data:
            distances = [np.linalg.norm(point - centroid) for centroid in centroids]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(point)
        return clusters

    def update_centroids(self, clusters):
        """Update the centroids as the mean of their respective clusters."""
        centroids = [np.mean(cluster, axis=0) for cluster in clusters if cluster]
        return centroids

    def fit(self, data):
        """Perform the K-means clustering."""
        centroids = self.initialize_centroids(data)

        for _ in range(self.max_iterations):
            clusters = self.assign_clusters(data, centroids)
            new_centroids = self.update_centroids(clusters)

            if np.all([np.array_equal(new, old) for new, old in zip(new_centroids, centroids)]):
                break  # Convergence achieved

            centroids = new_centroids

        self.centroids = centroids
        self.clusters = clusters

    def predict(self, data):
        """Predict the nearest cluster each data point belongs to."""
        predictions = []
        for point in data:
            distances = [np.linalg.norm(point - centroid) for centroid in self.centroids]
            cluster_idx = np.argmin(distances)
            predictions.append(cluster_idx)
        return predictions

# Example usage
data = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(k=2)
kmeans.fit(data)
print("Cluster centroids:", kmeans.centroids)
print("Predicted clusters:", kmeans.predict(data))
