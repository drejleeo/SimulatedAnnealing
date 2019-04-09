from matplotlib import pyplot as plt
from utils import plot_solution
import time
import random
import numpy


def anneal(T, min_T, alpha, iterations, distances, cities, dimension, plot=True):

    sol = random.sample(range(1, dimension + 1), dimension)
    best = sol
    old_cost = total_cost(sol, distances)
    if plot is True:
        fig = plt.figure()
        plot_solution(cities, sol, fig)

    while T > min_T:

        i = 1
        while i <= iterations:
            new_sol = get_neighbour(sol)
            new_cost = total_cost(new_sol, distances)
            if new_cost < old_cost:
                best = new_sol

            delta = delta_costs(new_cost, old_cost)
            ap = acceptance_probability(delta, T)

            if ap > random.random() or delta < 0:
                sol = new_sol
                old_cost = new_cost
                if plot is True:
                    plot_solution(cities, sol, fig)
            i += 1
        T = T * alpha

    if plot is True:
        plt.draw()
        time.sleep(10)
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
    return cost


def delta_costs(new_cost, old_cost):
    return new_cost - old_cost


def acceptance_probability(delta, T):
    e = numpy.exp(1)
    prob = e**(delta / T)
    return prob
