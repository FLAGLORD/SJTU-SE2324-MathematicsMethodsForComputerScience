import numpy as np
from fractions import Fraction
from matplotlib import pyplot as plt


def exe4():
    p = np.poly1d([1, Fraction(-29, 20), Fraction(29, 36), Fraction(-31, 144), Fraction(1, 36), Fraction(-1, 720)])
    print(p.roots)
    x = np.linspace(0, 1, 1001)
    y_reference = np.zeros(1001)
    plt.plot(x, p(x))
    plt.plot(x, y_reference)
    plt.show()

    # newton method
    p2 = np.polyder(p)
    x0 = 0.45
    x1 = x0 - p(x0)/p2(x0)

    while abs(x1-x0) > 1e-10:
        x0 = x1
        x1 = x0 - p(x0)/p2(x0)

    print("root searched using newton method:" + str(x1))

    # secant method

    x1 = 0
    x2 = 0.45
    while True:
        k = (p(x2) - p(x1))/(x2 - x1)
        b = p(x1) - k*x1
        x = -b/k
        if abs(p(x)) < 1e-11:
            break
        if (p(x) > 0 and p(x1) > 0) or (p(x) < 0 and p(x1 < 0)):
            x1 = x
        else:
            x2 = x

    print("root searched using secant method:" + str(x))




if __name__ == '__main__':
    exe4()
