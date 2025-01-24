import time, k_means_numpy, k_means_vanilla, create_cruster
from pprint import pprint

DATA = create_cruster.create_cluster(-100, 100, 4, 30000)

DATA_tuple = k_means_vanilla.denumpy_points(data=DATA)

print(f"Starting calculation for vanilla version...")
tV1 = time.time()
centroid_vanilla, group_vanilla = k_means_vanilla.k_means(data=DATA_tuple, k=4)
tV2 = time.time()
pprint(centroid_vanilla)
print(f"Finised, time taken: {tV2-tV1} sec.")

print(f"Starting calculation for numpy version...")
tN1 = time.time()
centroid_numpy, group_numpy = k_means_numpy.k_means(data=DATA, k=4)
tN2 = time.time()
pprint(centroid_numpy)
print(f"Finised, time taken: {tN2-tN1} sec.")

print("Time taken.")
print(f" .   Vanilla: {tV2-tV1} sec.")
print(f" .   Numpy:   {tN2-tN1} sec.")