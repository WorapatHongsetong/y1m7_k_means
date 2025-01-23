import numpy as np
import matplotlib.pyplot as plt
import random


def choose_centers(min: float, max: float, num: int) -> np.array:
    centers = np.random.uniform(min, max, size=(num, 2))
    
    return centers

def generate_around_centers(centers: np.array, num_avg: float, distance: float) -> np.array:
    num_left  = num_avg

    for _ in range(len(centers)):
        num_var = np.random.random_integers(0, int(num_left))
        num_left -= num_var
        
        for _ in range(num_var):
            print(num_var)
            

if __name__ == "__main__":
    centers = choose_centers(-1, 1, 3)
    print(centers)

    # crusters = generate_around_centers(centers=centers, num_avg=20, distance=0.5)
    crusters = generate_around_centers(centers=[1, 2, 3], num_avg=100, distance=None)

    plt.scatter(crusters)
    plt.show()
