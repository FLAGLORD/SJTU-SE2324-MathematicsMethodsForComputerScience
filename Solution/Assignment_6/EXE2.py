import scipy
import numpy as np
from matplotlib import pyplot as plt
from sympy import simplify, sin, pi, sqrt, symbols, diff


# def exe_2_1():
#     x = symbols('x', real=True)
#     n = symbols('n', positive=True)
#     psi_func = sqrt(2)*sin(pi*n*x)
#     eigenvalue = -(n**2)*(pi**2)
#     print(simplify(diff(psi_func, x, 2)-eigenvalue*psi_func))

def matrix_laplacian(N):
    A = np.arange(N * N).reshape(N, N)
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i, j] = -2
            elif np.abs(i - j) == 1:
                A[i, j] = 1
            else:
                A[i, j] = 0
    return A


def psi_func(x, n):
    return np.sqrt(2) * np.sin(np.pi * n * x)


def exe_2_3():
    # x = symbols('x', real=True)
    # y = sqrt(2) * sin(pi * x)
    # M = diff(y, x, 2)
    # k = pi
    # print(y)
    # print(M)
    # print(simplify(M + (k ** 2) * y))
    N = 99
    h = 0.01
    x = np.arange(0, 1, h)
    x = np.delete(x, 0, None)
    y = psi_func(x, 1)
    A = matrix_laplacian(N)
    M = np.power(h, -2) * A
    zero = np.linspace(0, 0, 99)
    print(np.allclose(zero, np.dot(M, y) + np.pi ** 2 * y, atol=1e-02))


def exe_2_4():
    N = 99
    h = 0.01
    x = np.arange(0, 1, h)
    x = np.delete(x, 0, None)
    A = matrix_laplacian(N)
    M = np.power(h, -2) * A
    eigenvalues, eigenvectors = np.linalg.eig(M)

    idx = np.argsort(eigenvalues)
    eigenvalues.sort()
    eigenvectors_selected = [eigenvectors[:, idx[-1]], eigenvectors[:, idx[-2]], eigenvectors[:, idx[-3]]]
    print('The 3 eigenvalues with the smallest magnitude are')
    print(eigenvalues[::-1][0:3])
    plt.plot(x, eigenvectors_selected[0], 'r', label=r'$-\pi^2$')
    plt.plot(x, eigenvectors_selected[1], 'y', label=r'$-4\pi^2$')
    plt.plot(x, eigenvectors_selected[2], 'b', label=r'$-9\pi^2$')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # exe_2_3()
    exe_2_4()
