# EXE_3
# Numerics and Linear Algebra
import numpy as np
import numpy.polynomial.polynomial as npp
import math
from matplotlib import pyplot as plt
from scipy.linalg import lu, solve, cholesky
from numpy import linalg as LA
import prettytable as pt
from scipy import integrate


def f(x):
    return 1.0 / (1.0 + np.power(x, 2))


def sample_data(N):
    x_n = np.linspace(0, 1, N)
    y_n = f(x_n)
    return x_n, y_n


def fourier_matrix(N):
    x_n, y_n = sample_data(N)
    generate_val = []

    for x_i in x_n:
        for j in range(1, int(N / 2) + 1):
            generate_val.append(np.sin(j * np.pi * x_i))
        for j in range(int(N / 2) + 1, N + 1):
            generate_val.append(np.cos((j - N / 2) * np.pi * x_i))

    return np.array(generate_val).reshape(N, N)


def vandermonde_matrix(N):
    x_n, y_n = sample_data(N)
    return npp.polyvander(x_n, N - 1)


def solve_by_lu(N):
    # sample data
    # M = N
    x_n, y_n = sample_data(N)

    # Vandermonde matrix
    v_n = npp.polyvander(x_n, N - 1)
    # use lu to decompose
    p, l, u = lu(v_n)

    # now we have PLU c_n = y_n
    # take U c_n as intermediate, solve PL intermediate = y_n
    inter = solve(p.dot(l), y_n)

    # solve U c_n = intermediate
    c_n = solve(u, inter)
    return c_n


# use coefficient to calculate f, and it's for vandermonde
def fit_f(x, c):
    result = 0.0
    index = 0
    for val in np.nditer(c):
        result += val * np.power(x, index)
        index += 1
    return result


# use coefficient to calculate f, and it's for fourier
def fit_f_fourier(x, c):
    result = 0.0
    N = c.shape[1]
    with np.nditer(c) as it:
        for j in range(1, int(N / 2) + 1):
            result += it[0] * np.sin(j * np.pi * x)
            it.iternext()
        for j in range(int(N / 2) + 1, N + 1):
            result += it[0] * np.cos((j - N / 2) * np.pi * x)
            it.iternext()

    return result


def residual_l2_norm(c, x, y):
    # y_predict = fit_f(x, c)
    # residual = y_predict - y
    residual = x.dot(c) - y
    # print(residual)
    return LA.norm(residual, 2)


def is_pos_def(A):
    return np.all(np.linalg.eigvals(A) > 0)


def gram_matrix(A):
    return A.T.dot(A)


def solution_3_1():
    tb = pt.PrettyTable()
    tb.field_names = ['N', 'monomial coefficient', 'residual L2 Norm']
    # M = N = 8
    c_8 = solve_by_lu(8)
    x_8, y_8 = sample_data(8)
    tb.add_row([8, c_8, residual_l2_norm(c_8, vandermonde_matrix(8), y_8)])

    # M = N = 16
    c_16 = solve_by_lu(16)
    x_16, y_16 = sample_data(16)
    tb.add_row([16, c_16, residual_l2_norm(c_16, vandermonde_matrix(16), y_16)])
    print(tb)


    x = np.linspace(0, 1, 100)
    plt.plot(x, f(x), label='reference')
    plt.plot(x, fit_f(x, c_8), label='N = 8')
    plt.plot(x, fit_f(x, c_16), label='N = 16')
    plt.legend()
    plt.show()


def solution_3_2():
    x = np.arange(4, 34, 2)
    y1 = np.array([LA.cond(vandermonde_matrix(N)) for N in x])
    y2 = np.array([LA.cond(fourier_matrix(N)) for N in x])

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('N')
    ax1.set_ylabel('cond(V)')
    ax1.set_yscale('log')
    ax1.scatter(x, y1, marker='x')
    ax1.set_title('N vs. cond(V)')

    fig, ax2 = plt.subplots()
    ax2.set_xlabel('N')
    ax2.set_ylabel('cond(F)')
    ax2.set_yscale('log')
    ax2.scatter(x, y2, marker='x')
    ax2.set_title('N vs. cond(F)')

    plt.show()


def generate_tb_row(N):
    row = [N]
    v_n = vandermonde_matrix(N)
    F_n = fourier_matrix(N)
    gram_A_V = gram_matrix(v_n)
    gram_A_F = gram_matrix(F_n)
    row.append(is_pos_def(gram_A_V))
    row.append(is_pos_def(gram_A_F))
    row.append(LA.cond(v_n))
    row.append(LA.cond(F_n))
    return row


def solution_3_3():
    # similar to solution_3_2
    x = np.arange(4, 34, 2)
    tb = pt.PrettyTable()
    tb.field_names = ['N', 'isposdef(Av)', 'isposdef(AF)', 'cond(V)', 'cond(F)']
    for N in x:
        tb.add_row(generate_tb_row(N))

    print(tb)


def solve_by_cholesky(A, b):
    l = LA.cholesky(A)
    # now we have A = LLT, LLT x = b
    # take LT x as y, solve L y = b
    y = solve(l, b)
    # solve LT x = y
    x = solve(l.T, y)
    return x


def solution_3_4():
    tb1 = pt.PrettyTable()
    tb2 = pt.PrettyTable()
    tb1.field_names = ['N', 'V', 'residual L2 Norm(V)']
    tb2.field_names = ['N', 'F', 'residual L2 Norm(F)']

    row1 = [8]
    row2 = [8]
    v_8 = vandermonde_matrix(8)
    F_8 = fourier_matrix(8)
    x_8, y_8 = sample_data(8)
    c_vandermonde = solve_by_cholesky(v_8.T.dot(v_8), v_8.T.dot(y_8))
    c_fourier = solve_by_cholesky(F_8.T.dot(F_8), F_8.T.dot(y_8))
    row1.append(c_vandermonde)
    row2.append(c_fourier)
    residual_vandermonde = residual_l2_norm(c_vandermonde, v_8, y_8)
    residual_fourier = residual_l2_norm(c_fourier, F_8, y_8)
    row1.append(residual_vandermonde)
    row2.append(residual_fourier)
    tb1.add_row(row1)
    tb2.add_row(row2)
    print(tb1)
    print(tb2)


if __name__ == '__main__':
    # solution_3_1()
    # solution_3_2()
    # solution_3_3()
    solution_3_4()
