from models import City
import re
from cost_algorithms import ALGORITHMS


def generate_section(file_descriptor, end_mark, regex_pattern): # generate sections in order to read them
    line = file_descriptor.readline().strip()

    while end_mark not in line:
        regex = re.search(regex_pattern, line).groups()
        yield regex
        line = file_descriptor.readline().strip()


def process_data(file_path):    # read and process data into dictionaries
    with open(file_path, 'r') as file:
        listify_headers = generate_section(
            file_descriptor=file,
            end_mark='NODE_COORD_SECTION',
            regex_pattern='(.*): (.*)'
        )
        listify_intel = generate_section(
            file_descriptor=file,
            end_mark='EOF',
            regex_pattern='(\d*) (\d*) (\d*)'
        )
        headers = {key: value for (key, value) in listify_headers}
        headers['DIMENSION'] = int(headers['DIMENSION'])

        intel = {int(order_nr): City(int(x_coord), int(y_coord)) for (order_nr, x_coord, y_coord) in listify_intel}

    return headers, intel
