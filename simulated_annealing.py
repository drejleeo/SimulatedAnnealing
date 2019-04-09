from random import random
from cost_algorithms import ALGORITHMS
import numpy


def anneal(T, min_T, alpha, iterations, distances):

    sol = numpy.random.permutation(distances.nr_of_cities)
    old_cost = total_cost(sol, distances)
    while T > min_T:
        i = 1
        while i <= iterations:
            new_sol = neighbor(sol)
            new_cost = total_cost(new_sol, distances)
            ap = acceptance_probability(new_cost, old_cost, T)
            if ap > random():
                sol = new_sol
                old_cost = new_cost
            i += 1
        T = T * alpha
    return sol, total_cost(sol, distances)


def total_cost(solution, distances):
    cost = 0
    for index in range(len(solution) - 1):
        cost += distances.get_between_cities(index, index + 1)
    cost += distances.get_between_cities(solution[-1], solution[0])
    return cost


def acceptance_probability(new_cost, old_cost, T):
    e = numpy.exp(1)
    return e**((new_cost - old_cost) / T)
