import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from concurrent.futures import ThreadPoolExecutor
import logging


class KMeansClustering:
    """Class for performing K-Means Clustering on a dataset."""

    def __init__(self, data: pd.DataFrame):
        """
        Initializes KMeansClustering with data.

        Args:
            data (pd.DataFrame): The dataset to cluster.
        """
        self.data = data
        self.data_numeric = data.select_dtypes(include=[np.number])
        self.scaled_data = None
        self.cluster_labels = None
        logging.info("Initialized KMeansClustering class.")

    def scale_data(self):
        """Scales the data using StandardScaler."""
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.data_numeric)
        logging.info("Data has been scaled using StandardScaler.")

    def elbow_plot(self, max_clusters: int):
        """
        Plots the Elbow Plot for the data using multi-threading.

        Args:
            max_clusters (int): Maximum number of clusters to consider.
        """
        logging.info("Started generating the Elbow Plot.")
        wcss = []
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.calculate_wcss, i)
                for i in range(1, max_clusters + 1)
            ]
            for future in futures:
                wcss.append(future.result())

        plt.plot(range(1, max_clusters + 1), wcss)
        plt.title("Elbow Plot")
        plt.xlabel("Number of Clusters")
        plt.ylabel("WCSS")
        plt.show()
        logging.info("Elbow Plot generated and displayed.")

    def calculate_wcss(self, num_clusters: int) -> float:
        """
        Calculates the WCSS for a given number of clusters.

        Args:
            num_clusters (int): The number of clusters for which to calculate WCSS.

        Returns:
            float: The calculated WCSS value.
        """
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        kmeans.fit(self.scaled_data)
        logging.info(f"WCSS calculated for {num_clusters} clusters.")
        return kmeans.inertia_

    def cluster_data(self, num_clusters: int) -> pd.DataFrame:
        """
        Clusters the data using K-Means Clustering.

        Args:
            num_clusters (int): The number of clusters to use for K-Means.

        Returns:
            pd.DataFrame: The original data with an additional column for cluster labels.
        """
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        kmeans.fit(self.scaled_data)
        self.cluster_labels = kmeans.labels_
        self.data["Cluster"] = self.cluster_labels
        logging.info(f"Data has been clustered into {num_clusters} clusters.")
        return self.data
