from simulated_annealing import anneal
from models import Distances
from utils import process_data
import sys, os

base_path = os.getcwd()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rel_path = sys.argv[1]
    else: rel_path = 'wef/kroA100.tsp'
    full_path = '/'.join((base_path, rel_path))
    headers, cities = process_data(file_path=full_path)

    dists = Distances(
        cities=cities,
        total=headers['DIMENSION'],
        custom_alg=headers['EDGE_WEIGHT_TYPE'],
    )

    solution = anneal(
        T=1.0,
        min_T=0.00001,
        alpha=0.9,
        iterations=100,
        distances=dists,
        cities=cities,
        dimension=headers['DIMENSION'],
        plot=True,
    )

    print(solution)
