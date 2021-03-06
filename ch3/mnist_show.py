# coding: utf-8
import os
from sys import path
import numpy as np
from PIL import Image

path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
from dataset.mnist import load_mnist


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def main():
    mnist = load_mnist(flatten=True, normalize=False)
    (x_train, t_train), (x_test, t_test) = mnist

    img = x_train[0]
    label = t_train[0]
    print(label)  # 5

    print(img.shape)  # (784,)
    img = img.reshape(28, 28)  # 形状を元の画像サイズに変形
    print(img.shape)  # (28, 28)

    img_show(img)


if __name__ == "__main__":
    main()
