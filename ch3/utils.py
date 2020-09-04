# coding: utf-8
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# def softmax(x):
#     exp_x = np.exp(x)
#     total_exp_x = np.sum(exp_x)
#     y = exp_x / total_exp_x
#     return y


# for overflow
def safe_softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    total_exp_x = np.sum(exp_x)
    y = exp_x / total_exp_x
    return y
