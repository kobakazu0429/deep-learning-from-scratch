# coding: utf-8
import os
from sys import path
import numpy as np

path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss


def main():
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])

    net = simpleNet()

    f = lambda w: net.loss(x, t)
    dW = numerical_gradient(f, net.W)

    print(dW)


if __name__ == "__main__":
    main()
