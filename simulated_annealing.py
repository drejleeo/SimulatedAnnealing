from copy import deepcopy

from matplotlib import pyplot as plt
from utils import plot_solution
import time
import random
import numpy


def anneal(T, min_T, alpha, iterations, distances, cities, dimension, plot=False):

    sol = random.sample(range(1, dimension + 1), dimension)
    old_cost = total_cost(sol, distances)

    best = sol
    best_cost = old_cost
    if plot is True:
        fig = plt.figure()
        fig.show()
        plot_solution(cities, sol, fig)

    while T > min_T:

        i = 1
        while i <= iterations:
            new_sol_copy = deepcopy(sol)
            new_sol = get_neighbour(new_sol_copy)
            new_cost = total_cost(new_sol, distances)
            if new_cost < best_cost:
                best = deepcopy(new_sol)
                best_cost = new_cost

            delta = delta_costs(new_cost, old_cost)
            ap = acceptance_probability(delta, T)
            print("Old_cost {} new_cost {} Temp: {} ap {}".format(old_cost, new_cost, T, ap))

            if delta < 0 or ap > random.random():
                sol = new_sol
                old_cost = new_cost
                if plot is True:
                    plot_solution(cities, sol, fig)
                    plt.pause(0.01)

            i += 1
        T = T * alpha

    if plot is True:
        plt.draw()
        time.sleep(5)
    print('Best distance: ', total_cost(best, distances))
    return sol, total_cost(sol, distances)


def get_neighbour(solution):
    """
    Function generates 2 random numbers and swaps the two cities with the 2 generated indexes.
    :param solution: A permutation representing a solution, not necessarily good.
    :return: A neighbour solution created by 2-swapping 2 cities
    """
    index1 = random.randint(0, len(solution) - 1)
    index2 = random.randint(0, len(solution) - 1)
    solution[index1], solution[index2] = solution[index2], solution[index1]
    return solution


def total_cost(solution, distances):
    cost = 0
    for index in range(len(solution) - 1):
        cost += distances.get_between_cities(solution[index], solution[index + 1])
    cost += distances.get_between_cities(solution[-1], solution[0])
    return round(cost, 2)


def delta_costs(new_cost, old_cost):
    return new_cost - old_cost


def acceptance_probability(delta, T):
    e = numpy.exp(1)
    prob = e**(-delta / T)
    return prob
