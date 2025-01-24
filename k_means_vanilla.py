import numpy as np
import matplotlib.pyplot as plt
import create_cruster, random, math
from pprint import pprint

def denumpy_points(data: np.array):
    result = []
    for point in data:
        result.append((float(point[0]), float(point[1])))
    return tuple(result)

import random
import math

def k_means(data, k, min_iters=500, error=1e-4):
    centroids = [random.choice(data) for _ in range(k)]
    
    old_centroids = []

    cluster_assignments = [None] * len(data)
    
    iterations = 0
    
    while iterations < min_iters or not all(
        math.isclose(c1[0], c2[0], abs_tol=error) and math.isclose(c1[1], c2[1], abs_tol=error)
        for c1, c2 in zip(centroids, old_centroids)
    ):
        iterations += 1
        
        for i, point in enumerate(data):
            distances = [math.dist(point, centroid) for centroid in centroids]
            cluster_assignments[i] = distances.index(min(distances))
        
        old_centroids = [tuple(centroid) for centroid in centroids]
        
        for i in range(k):
            assigned_points = [point for j, point in enumerate(data) if cluster_assignments[j] == i]
            
            if assigned_points:
                new_centroid = [sum(coord) / len(assigned_points) for coord in zip(*assigned_points)]
                centroids[i] = new_centroid

    print(f"Total: {iterations} terations")    

    return centroids, cluster_assignments



if __name__ == "__main__":
    clusters = denumpy_points(create_cruster.create_cluster(-100, 100, 4, 300))
    centroids, cluster_group = k_means(clusters, 4)

    pprint(cluster_group)


    colors = (
        'lightblue',
        'lightgreen',
        'lightpink',
        'lightyellow',
        'lavender',
        'seashell',
        'salmon'
    )

    for i in range(len(clusters)):
        for j in set(cluster_group):
            if cluster_group[i] == j:
                plt.scatter(clusters[i][0], clusters[i][1], c=colors[j])

    for point in centroids:
        plt.scatter(point[0], point[1], c="black")

    plt.show()
    