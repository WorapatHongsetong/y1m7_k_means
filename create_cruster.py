import numpy as np
import matplotlib.pyplot as plt
import random


def choose_centers(min: float, max: float, num: int) -> np.array:
    centers = np.random.uniform(min, max, size=(num, 2))
    
    return centers

import numpy as np

def generate_around_centers(centers: np.array, num_avg: int, distance: float) -> np.array:
    num_left = num_avg
    all_clusters = []

    for center in centers:
        num_var = np.random.randint(0, num_left // np.e)
        num_left -= num_var
        dist_err = np.random.uniform(0.5, 2*np.e)
        points = []
        while len(points) < num_var:
            x_i = np.random.uniform(center[0] - distance * dist_err, center[0] + distance * dist_err, num_var)
            y_i = np.random.uniform(center[1] - distance * dist_err, center[1] + distance * dist_err, num_var)

            dist_sq = (x_i - center[0]) ** 2 + (y_i - center[1]) ** 2
            valid_points = (dist_sq <= distance ** 2)

            points.append(np.column_stack((x_i[valid_points], y_i[valid_points])))

        cluster = np.vstack(points)
        all_clusters.append(cluster)

    min_x = np.min(centers[:, 0]) - distance
    max_x = np.max(centers[:, 0]) + distance
    min_y = np.min(centers[:, 1]) - distance
    max_y = np.max(centers[:, 1]) + distance

    noise_x = np.random.uniform(min_x, max_x, num_left)
    noise_y = np.random.uniform(min_y, max_y, num_left)

    noise_points = np.column_stack((noise_x, noise_y))
    all_clusters.append(noise_points)

    all_clusters = np.vstack(all_clusters)

    print(all_clusters)
    print(f"Total points: {len(all_clusters)}")

    return all_clusters
           
def create_cluster(num_centers: int, num_points: int, min_v: float, max_v: float, distance: float) -> np.array:
    return generate_around_centers(centers=choose_centers(min=min_v, max=max_v, num=num_centers), num_avg=num_points, distance=distance)



if __name__ == "__main__":
    centers = choose_centers(0, 100, 4)
    print(centers)

    clusters = generate_around_centers(centers=centers, num_avg=300, distance=30)

    clusters = create_cluster(num_centers=4, num_points=300, min_v=0, max_v=100, distance=30)

    plt.scatter(clusters[:, 0], clusters[:, 1])
    plt.show()
