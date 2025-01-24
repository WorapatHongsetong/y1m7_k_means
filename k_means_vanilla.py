import numpy as np
import matplotlib.pyplot as plt
import create_cruster, random, math

def denumpy_points(data: np.array):
    result = []
    for point in data:
        result.append((float(point[0]), float(point[1])))
    return tuple(result)

import random
import math

def k_means(data, k, max_iters=100, error=1e-4):
    centroids = [random.choice(data) for _ in range(k)]
    
    old_centroids = []

    cluster_assignments = [None] * len(data)
    
    for _ in range(max_iters):
        for i, point in enumerate(data):
            distances = [math.dist(point, centroid) for centroid in centroids]
            cluster_assignments[i] = distances.index(min(distances))
        
        old_centroids = [tuple(centroid) for centroid in centroids]
        
        for i in range(k):
            assigned_points = [point for j, point in enumerate(data) if cluster_assignments[j] == i]
            
            if assigned_points:
                new_centroid = [sum(coord) / len(assigned_points) for coord in zip(*assigned_points)]
                centroids[i] = new_centroid
        
        if all(
            math.isclose(c1[0], c2[0], abs_tol=error) and math.isclose(c1[1], c2[1], abs_tol=error)
            for c1, c2 in zip(centroids, old_centroids)
        ):
            break
    
    return centroids, cluster_assignments


if __name__ == "__main__":
    clusters = denumpy_points(create_cruster.create_cluster(-100, 100, 4, 300))
    centroids = k_means(clusters, 4)[0]

    for point in clusters:
        plt.scatter(point[0], point[1], c="lightblue")

    for point in centroids:
        plt.scatter(point[0], point[1], c="blue")

    plt.show()
    