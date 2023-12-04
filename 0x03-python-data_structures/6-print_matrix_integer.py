#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            if elem != 0:
                print("{:d}".format(elem), end=" ")
        print("")
