# EXE_4
#  Least Squares Problems and QR
import numpy as np
import numpy.polynomial.polynomial as npp
from matplotlib import pyplot as plt
from numpy import linalg as LA
import prettytable as pt


def f(x):
    return 1.0 / (1.0 + np.power(x, 2))


def gv_predict(x, c):
    result = 0.0
    index = 0
    for val in np.nditer(c):
        result += val * np.power(x, index)
        index += 1
    return result


def gf_predict(x, c):
    result = 0.0
    N = c.shape[1]
    print(c)
    with np.nditer(c) as it:
        for j in range(1, int(N / 2) + 1):
            result += it[0] * np.sin(j * np.pi * x)
            it.iternext()
        for j in range(int(N / 2) + 1, N + 1):
            result += it[0] * np.cos((j - N / 2) * np.pi * x)
            it.iternext()

    return result


def sample_data(N):
    x_n = np.linspace(0, 1, N)
    y_n = f(x_n)
    return x_n, y_n


# get Vandermonde matrix, but M ≠ N
def vandermonde_matrix(N, M):
    x_n, y_n = sample_data(M)
    # print(npp.polyvander(x_n, N-1).shape)
    return npp.polyvander(x_n, N - 1)


def fourier_matrix(N, M):
    x_n, y_n = sample_data(M)
    generate_val = []

    for x_i in x_n:
        for j in range(1, int(N / 2) + 1):
            generate_val.append(np.sin(j * np.pi * x_i))
        for j in range(int(N / 2) + 1, N + 1):
            generate_val.append(np.cos((j - N / 2) * np.pi * x_i))

    return np.array(generate_val).reshape(M, N)


def solve_by_qr(v, M):
    # solution x = (AT A)-1 AT b
    x_n, y_n = sample_data(M)
    Q, R = LA.qr(v)
    # now x = R-1 QT b
    return np.mat(R).I.dot(Q.T).dot(y_n)


def solution_4_1():
    tb = pt.PrettyTable()
    tb.field_names = ['M', 'N', 'monomial coefficient']
    # M = 16, N = 4
    v_16_4 = vandermonde_matrix(4, 16)
    c_16_4 = solve_by_qr(v_16_4, 16)

    # M = 16, N = 8
    v_16_8 = vandermonde_matrix(8, 16)
    c_16_8 = solve_by_qr(v_16_8, 16)
    tb.add_row([16, 4, c_16_4])
    tb.add_row([16, 8, c_16_8])
    print(tb)
    return c_16_4, c_16_8


def solution_4_2():
    tb = pt.PrettyTable()
    tb.field_names = ['M', 'N', 'monomial coefficient(F)']
    x_ref = np.linspace(0, 1, 100)
    plt.plot(x_ref, f(x_ref), label='reference', color='dodgerblue')
    c_16_4, c_16_8 = solution_4_1()

    # M = 16, N = 4
    f_16_4 = fourier_matrix(4, 16)
    c_16_4_f = solve_by_qr(f_16_4, 16)

    # M = 16, N = 8
    f_16_8 = fourier_matrix(8, 16)
    c_16_8_f = solve_by_qr(f_16_8, 16)
    tb.add_row([16, 4, c_16_4_f])
    tb.add_row([16, 8, c_16_8_f])
    print(tb)

    x_16, _ = sample_data(16)

    y_c_16_4 = np.array([gv_predict(x, c_16_4) for x in x_16])
    y_c_16_8 = np.array([gv_predict(x, c_16_8) for x in x_16])
    y_f_16_4 = np.array([gf_predict(x, c_16_4_f) for x in x_16])
    y_f_16_8 = np.array([gf_predict(x, c_16_8_f) for x in x_16])

    plt.scatter(x_16, y_c_16_4, label=r'$N = 4,g_V$', marker='x', color='m')
    plt.scatter(x_16, y_c_16_8, label=r'$N = 8,g_V$', marker='.', color='m')

    plt.scatter(x_16, y_f_16_4, label=r'$N = 4,g_F$', marker='x', color='c')
    plt.scatter(x_16, y_f_16_8, label=r'$N = 8,g_F$', marker='.', color='c')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    solution_4_2()
