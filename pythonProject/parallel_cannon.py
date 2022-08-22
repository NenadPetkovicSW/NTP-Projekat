import csv
from math import sqrt
import numpy as np
import multiprocessing as mp
import time


def create_iteration_file():
    """
    Create initial output file for parallel_iterations.
    :return:
    """
    with open('parallel_iterations.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['result'])


def append_iteration_file(matrix):
    """
    Append to sequential_iterations.
    :param matrix:
    :return:
    """
    with open('parallel_iterations.csv', 'a+', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([matrix])


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


def multiplication(matrix_1, matrix_2, row_number, colon_number):
    """
    This function is used for parallel multiplication of processes...
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
    for k in range(row_number, row_number + n_p_sqrt):
        for l in range(colon_number, colon_number + n_p_sqrt):
            result[k][l] += thread[0][k - row_number][l - colon_number]
    append_iteration_file(result)
    return result


def multiplication_parallel(matrix_1, matrix_2, n, p, processors):
    """
    This function is used for parallel multiplication using Cannon’s algorithm...
    :param processors:
    :param matrix_1:
    :param matrix_2:
    :param n:
    :param p:
    :return:
    """
    create_iteration_file()

    start_time = time.time()

    # serial_time = time.time()
    result = np.zeros((n, n))

    pool = mp.Pool(processors)

    # serial_time_count = time.time() - serial_time
    matrix_1, matrix_2 = pool.apply_async(shift, args=(matrix_1, matrix_2, n, 2)).get()
    serial_time = time.time()
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

                # serial_time_count = serial_time_count + (time.time() - serial_time)
                threads.append(pool.apply_async(multiplication, args=(m1, m2, row_number, colon_number)))
                matrix_1, matrix_2 = pool.apply_async(shift, args=(matrix_1, matrix_2, n, 1)).get()
                # serial_time = time.time()

    for thread in threads:
        result = add_result(thread.get(), result, n_p_sqrt)

    # serial_time_count = serial_time_count + (time.time() - serial_time)
    pool.terminate()
    pool.close()
    pool.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nParallel elapsed time: {0}\n".format(str(elapsed_time)))

    # serial_pre = (serial_time_count * (100 / elapsed_time)) / 100
    # print("\nParallel serial time: {0}\n".format(str(serial_pre)))
    # #
    # print("\nParallel parallel time: {0}\n".format(str(1 - serial_pre)))
    # #
    # print("\nParallel speedup time: {0}\n".format(str((serial_pre + (1 - serial_pre) * processors))))
