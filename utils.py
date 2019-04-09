from models import City
import re
from matplotlib import pyplot as plt


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


def plot_solution(cities, solution, fig):
    plot_x_coords = []
    plot_y_coords = []

    for index in range(len(solution)):
        current_node = cities[solution[index]]

        plot_x_coords.append(int(current_node.x_coord))
        plot_y_coords.append(int(current_node.y_coord))

    plot_x_coords.append(cities[solution[0]].x_coord)
    plot_y_coords.append(cities[solution[0]].y_coord)

    plt.clf()
    plt.plot(plot_x_coords,plot_y_coords)
    fig.canvas.draw()
