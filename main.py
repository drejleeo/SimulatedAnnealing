import numpy

from simulated_annealing import anneal
from models import Distances
from utils import process_data
from cost_algorithms import ALGORITHMS
import sys, os

base_path = os.getcwd()
rel_path = sys.argv[1]


if __name__ == '__main__':
    full_path = '/'.join((base_path, rel_path))
    headers, cities = process_data(file_path=full_path)

    distances = Distances(
        cities=cities,
        total=headers['DIMENSION'],
        custom_alg=headers['EDGE_WEIGHT_TYPE'],
    )

    solution = anneal(
        T=1.0,
        min_T=0.00001,
        alpha=0.9,
        iterations=100,
        cost_alg=ALGORITHMS[headers['EDGE_WEIGHT_TYPE']],
        dimension=headers['DIMENSION'],
    )

    print(solution)
