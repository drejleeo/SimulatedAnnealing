from random import random
from cost_algorithms import ALGORITHMS
import numpy


def anneal(T, min_T, alpha, cost_alg, sol):
    old_cost = cost_alg(sol)
    while T > min_T:
        i = 1
        while i <= 100:
            new_sol = neighbor(sol)
            new_cost = cost_alg(new_sol)
            ap = acceptance_probability(new_cost, old_cost, T)
            if ap > random():
                sol = new_sol
                old_cost = new_cost
            i += 1
        T = T * alpha
    return sol, cost


def acceptance_probability(new_cost, old_cost, T):
    e = numpy.exp(1)
    return e**((new_cost - old_cost) / T)
