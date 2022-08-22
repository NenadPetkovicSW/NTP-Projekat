import csv
from math import sqrt
import numpy as np
import time


def create_iteration_file():
    """
    Create initial output file for sequential_iterations.
    :return:
    """
    with open('sequential_iterations.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['result_matrix'])


def append_iteration_file(matrix):
    """
    Append to sequential_iterations.
    :param matrix:
    :return:
    """
    with open('sequential_iterations.csv', 'a+', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([matrix])


def multiplication_sequential(matrix_1, matrix_2, n):
    """
    This function is used for sequential multiplication using Cannon’s algorithm...
    :param matrix_1:
    :param matrix_2:
    :param n:
    :return:
    """
    create_iteration_file()
    start_time = time.time()
    result_matrix = np.zeros((n, n))

    # p is equal to n because we have n processes
    p = n

    # performing initial shift, first we shift left then we shift up
    for i in range(n):
        matrix_1[i] = np.roll(matrix_1[i], -i)
        matrix_2[:, i] = np.roll(matrix_2[:, i], -i)

    # p sequential iterations, first we are doing multiplication, then we perform shift by 1 left and up
    for k in range(p):
        for i in range(n):
            for j in range(n):
                result_matrix[i][j] += matrix_1[i][j] * matrix_2[i][j]
        for i in range(n):
            matrix_1[i] = np.roll(matrix_1[i], -1)
            matrix_2[:, i] = np.roll(matrix_2[:, i], -1)

        append_iteration_file(result_matrix)

    end_time = time.time()

    elapsed_time = end_time - start_time

    print("\nSequential elapsed time: {}\n".format(str(elapsed_time)))


def shift(matrix_1, matrix_2, n, s):
    """
    Function for matrix shifting.
    First we shift left for provided steps, then we shift up
    :param matrix_1: matrix one
    :param matrix_2: matrix two
    :param n: n of the matrix
    :param s: step of shifting
    :return: matrix_1 and matrix_2 shifted
    """
    for i in range(n):
        matrix_1[i] = np.roll(matrix_1[i], -s)
        matrix_2[:, i] = np.roll(matrix_2[:, i], -s)
    return [matrix_1, matrix_2]


def multiplication_like_parallel(matrix_1, matrix_2, row_number, colon_number):
    """
    This function is used for sequential multiplication of processes...
    Function imitates parallel version.
    :param matrix_1:
    :param matrix_2:
    :param row_number:
    :param colon_number:
    :return:
    """
    n = len(matrix_1)
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            result[i][j] += matrix_1[i][j] * matrix_2[i][j]
    return [result, row_number, colon_number]


def add_result(thread, result, n_p_sqrt):
    """
    Function for tread reading. We read data provided from treads.
    Tis function prints results in a file.
    :param thread:
    :param result:
    :param n_p_sqrt:
    :return:
    """
    row_number = thread[1]
    colon_number = thread[2]
    for i in range(row_number, row_number + n_p_sqrt):
        for j in range(colon_number, colon_number + n_p_sqrt):
            result[i][j] += thread[0][i - row_number][j - colon_number]
    append_iteration_file(result)
    return result


def multiplication_sequential_like_parallel(matrix_1, matrix_2, n, p):
    """
    This function is used for sequential multiplication using Cannon’s algorithm...
    Tis function imitates parallel version.
    :param matrix_1:
    :param matrix_2:
    :param n:
    :param p:
    :return:
    """
    create_iteration_file()

    start_time = time.time()

    result = np.zeros((n, n))

    matrix_1, matrix_2 = shift(matrix_1, matrix_2, n, 2)

    threads = []
    p_sqrt = int(sqrt(p))
    n_p_sqrt = int(n / p_sqrt)
    for k in range(n):
        for i in range(p_sqrt):
            for j in range(p_sqrt):
                row_number = n_p_sqrt * i
                colon_number = n_p_sqrt * j
                m1 = matrix_1[row_number:(row_number + n_p_sqrt), colon_number:(colon_number + n_p_sqrt)]
                m2 = matrix_2[row_number:(row_number + n_p_sqrt), colon_number:(colon_number + n_p_sqrt)]

                threads.append(multiplication_like_parallel(m1, m2, row_number, colon_number))

                matrix_1, matrix_2 = shift(matrix_1, matrix_2, n, 1)

    for thread in threads:
        result = add_result(thread, result, n_p_sqrt)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nSequential elapsed time: {0}\n".format(str(elapsed_time)))
