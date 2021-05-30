# EXE_2
#  NumPy Warm-up
import numpy as np
import math
from matplotlib import pyplot as plt
from scipy import integrate


def gaussian(x, mean, variance):
    zeta = math.sqrt(2 * math.pi * variance)
    return 1. / zeta * np.exp(-np.power(x - mean, 2) / (2 * variance))


def verify(mean, variance):
    v, err = integrate.quad(gaussian, -10, 10, args=(mean, variance))
    print('mean = {0}, variance = {1}   :'.format(mean, variance), end='')
    # call numpy.isclose to check value
    print(np.isclose([v], [1.0]))


def main():
    x = np.linspace(-10, 10, 1000)

    plt.plot(x, gaussian(x, 0, 1), label=r'$\mu = 0, \sigma^2 = 1$')
    plt.plot(x, gaussian(x, 0, 2), label=r'$\mu = 0, \sigma^2 = 2$')
    plt.plot(x, gaussian(x, 0, 0.2), label=r'$\mu = 0, \sigma^2 = 0.2$')
    plt.plot(x, gaussian(x, 2, 1), label=r'$\mu = 2, \sigma^2 = 1$')
    plt.legend()

    # plt.show 会阻塞程序，所以先verify
    verify(0, 1)
    verify(0, 2)
    verify(0, 0.2)
    verify(2, 1)

    plt.show()


if __name__ == '__main__':
    main()
