from math import sqrt


def euc_2D(point1, point2):
    return sqrt(
        (point1[0] - point2[0])**2 + (point1[1]- point2[1])**2
    )


ALGORITHMS = {
    'EUC_2D': euc_2D,
}
