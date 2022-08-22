import numpy as np
import sequential_cannon
import parallel_cannon
import copy
from math import sqrt
import random


def insert_number(text):
    """ This is a function used to insert number and check if
        inserted number is int number.
        :param text
        :return:
    """
    while True:
        try:
            return_number = int(input(text))
            break
        except ValueError:
            print("You must insert a number...\n")
    return return_number


def print_matrix(matrix):
    """ This is a function used to print one matrix.
        :param matrix
        :return:
    """
    for m_i in range(0, len(matrix)):
        print(" ".join("{0:10}".format(m_j) for m_j in matrix[m_i]))


def create_matrix(n):
    """ This is a function used to create one matrix.
        You can select option to create matrix.
        1. Insert by hand
        2. Auto
        3. Matrix made of ones
        :param n
        :return:
    """
    print("Creating matrix:\n"
          "1. Insert by hand\n"
          "2. Auto\n"
          "3. Matrix made of ones\n")
    while True:
        option = insert_number("Insert number: ")
        if option == 1:
            return_matrix = []
            for m_i in range(0, n):
                return_matrix.append([])
                for m_j in range(0, n):
                    return_matrix[m_i].append(insert_number("M[{0}][{1}]: ".format(m_i, m_j)))
            break
        elif option == 2:
            return_matrix = [[random.randint(-(n ** 2), n ** 2) for _ in range(n)] for _ in range(n)]
            break
        elif option == 3:
            return_matrix = [[1] * n for _ in range(n)]
            break
        else:
            print("You must insert number from 1 to 3...\n")
    return return_matrix


def create_two_matrix(n):
    """ This is a function used to create one matrix.
        You can select option to create matrix.
        1. Insert by hand
        2. Auto
        3. Matrix made of ones
        :param n
        :return:
    """
    matrix_1 = create_matrix(n)
    print("Matrix first created...")
    # print_matrix(matrix1)

    matrix_2 = create_matrix(n)
    print("Matrix secound created...")
    # print_matrix(matrix2)

    return np.array(matrix_1, dtype=np.float64), np.array(matrix_2, dtype=np.float64)


def start():
    """ This is a function used start program.
        Matrix multiplication (Cannon’s algorithm).
        At the end we can see time needed for parallel and sequential multiplication
        :return:
    """
    print("Welcome!\nMatrix multiplication (Cannon’s algorithm): ")
    while True:
        n = insert_number("Insert n of the matrix: ")
        if n > 1:
            break
        print("N must be greater then 1...\n")

    while True:

        matrix1, matrix2 = create_two_matrix(n)
        # sequential_cannon.multiplication_sequential(copy.deepcopy(matrix1), copy.deepcopy(matrix2), n)
        while True:
            p = insert_number("Insert p: ")
            if p <= 1:
                print("p must be greater then 1!\n")
            elif sqrt(p) % 1 != 0:
                print("p must be perfect square!\n")
            elif n / sqrt(p) % 1 != 0:
                print("Sqrt(p) can't divide n!\n")
            else:
                break
        processors = insert_number("Insert number of processors: ")
        sequential_cannon.multiplication_sequential_like_parallel(copy.deepcopy(matrix1), copy.deepcopy(matrix2), n, p)
        parallel_cannon.multiplication_parallel(copy.deepcopy(matrix1), copy.deepcopy(matrix2), n, p, processors)

        break


if __name__ == '__main__':
    start()
