# coding: utf-8
import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = 1
    total = np.sum(w * x)
    if total >= 2:
        return 1
    else:
        return 0


def AND_bias(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    total = np.sum(w * x) + b
    if total <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y1 = AND(xs[0], xs[1])
        y2 = AND_bias(xs[0], xs[1])
        print(str(xs) + " -> " + str(y1) + ", " + str(y2))
