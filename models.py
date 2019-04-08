from cost_algorithms import ALGORITHMS


class City(object):
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return 'City with x={} and y={}'.format(self.x_coord, self.y_coord)


class Distances(object):
    def __init__(self, cities, total, custom_alg):
        self.all = {}
        for index1 in range(1, total + 1):
            for index2 in range(index1 + 1, total + 1):
                identifier = (index1, index2)
                point1 = (cities[index1].x_coord, cities[index1].y_coord)
                point2 = (cities[index2].x_coord, cities[index2].y_coord)

                self.all.update({
                    identifier: ALGORITHMS[custom_alg](point1, point2)
                })

    def get_between_cities(self, index1, index2):
        if index1 > index2:
            index1, index2 = index2, index1
        return self.all[(index1, index2)]
