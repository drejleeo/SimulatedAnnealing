from simulated_annealing import anneal
from models import Distances
from utils import process_data
import sys, os
import time
base_path = os.getcwd()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rel_path = sys.argv[1]
    else: rel_path = 'data/kroA100.tsp'
    full_path = '/'.join((base_path, rel_path))
    headers, cities = process_data(file_path=full_path)

    dists = Distances(
        cities=cities,
        total=headers['DIMENSION'],
        custom_alg=headers['EDGE_WEIGHT_TYPE'],
    )

    start = time.time()
    solution = anneal(
        T=10000,
        min_T=0.00001,
        alpha=0.99,
        iterations=100,
        distances=dists,
        cities=cities,
        dimension=headers['DIMENSION'],
        # plot=True,
    )
    print(time.time() - start)
