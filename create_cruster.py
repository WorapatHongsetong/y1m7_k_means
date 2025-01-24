import numpy as np
import matplotlib.pyplot as plt

def create_cluster(min, max, cen_num, pnt_num):
    centroids = np.random.uniform(min, max, size=(cen_num, 2))
    
    pnt_per_cluster = pnt_num // cen_num

    points = []

    for i in range(cen_num):
        std_dev = (max - min) / 10
        
        cluster_points = np.random.normal(loc=centroids[i], scale=std_dev, size=(pnt_per_cluster, 2))
        
        points.append(cluster_points)
    
    points = np.vstack(points)
    
    return points

if __name__ == "__main__":
    clusters = create_cluster(-100, 100, 4, 300)
    plt.scatter(clusters[:, 0], clusters[:, 1])
    plt.show()
