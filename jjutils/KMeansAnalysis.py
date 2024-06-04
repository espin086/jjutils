import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import concurrent.futures


class KMeansClustering:
    """Class for performing K-Means Clustering on a dataset."""

    def __init__(self, data):
        self.data = data.values
        self.data_numeric = None
        self.scaled_data = None
        self.cluster_labels = None

    def scale_data(self):
        """Scales the data using StandardScaler."""
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.data_numeric)

    def elbow_plot(self, max_clusters):
        """Plots the Elbow Plot for the data using multithreading."""
        wcss = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(1, max_clusters + 1):
                future = executor.submit(self.calculate_wcss, i)
                futures.append(future)
            for future in concurrent.futures.as_completed(futures):
                wcss.append(future.result())
        plt.plot(range(1, max_clusters + 1), wcss)
        plt.title("Elbow Plot")
        plt.xlabel("Number of Clusters")
        plt.ylabel("WCSS")
        plt.show()

    def calculate_wcss(self, num_clusters):
        """Calculates the WCSS for a given number of clusters."""
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        kmeans.fit(self.scaled_data)
        return kmeans.inertia_

    def cluster_data(self, num_clusters):
        """Clusters the data using K-Means Clustering."""
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        kmeans.fit(self.scaled_data)
        self.cluster_labels = kmeans.labels_
        self.data["Cluster"] = self.cluster_labels
        return self.data
