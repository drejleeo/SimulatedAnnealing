from models import Distances
from utils import process_data
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

    for item in distances.all.items():
        print(item)

    print(distances.get_between_cities(54, 3))
