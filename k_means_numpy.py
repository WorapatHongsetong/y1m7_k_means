import numpy as np
import matplotlib.pyplot as plt
import create_cruster, random, math
from pprint import pprint

import numpy as np

def k_means(data, k, min_iters=500, error=1e-4):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    
    old_centroids = np.zeros_like(centroids)
    
    cluster_assignments = np.zeros(data.shape[0])
    
    iterations = 0
    
    while iterations < min_iters or not np.all(np.abs(centroids - old_centroids) < error):
        iterations += 1
        for i, point in enumerate(data):
            distances = np.linalg.norm(point - centroids, axis=1)
            cluster_assignments[i] = np.argmin(distances)
        
        old_centroids = centroids.copy()
        
        for i in range(k):
            assigned_points = data[cluster_assignments == i]
            if len(assigned_points) > 0:
                centroids[i] = np.mean(assigned_points, axis=0)
        
        if np.all(np.abs(centroids - old_centroids) < error) and iterations > min_iters:
            print(f"Converged after {iterations} iterations.")
            break
    
    print(f"Total: {iterations} iterations.")

    return centroids, cluster_assignments


if __name__ == "__main__":
    clusters = create_cruster.create_cluster(-100, 100, 4, 300)

    centroids, clusters_group = k_means(clusters, 4)

    plt.scatter(clusters[:, 0], clusters[:, 1])
    plt.scatter(centroids[:, 0], centroids[:, 1], c="black")
    plt.show()