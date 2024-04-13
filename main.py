import numpy as np


def adding_matrix(m1, m2):
    return np.add(m1, m2)


def subtract_matrix(m1, m2):
    return np.subtract(m1, m2)


def multiple_matrix(m1, m2):
    return np.multiply(m1, m2)


def divide_matrix(m1, m2):
    return np.divide(m1, m2)


def input_matrix(r, c):
    matrix = []
    print(f"Enter {r}x{c} matrix elements")
    for i in range(r):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)


def program():
    r1 = int(input("Enter number of rows of 1 matrix: "))
    c1 = int(input("Enter number of columns of 1 matrix: "))
    r2 = int(input("Enter number of rows of 2 matrix: "))
    c2 = int(input("Enter number of columns of 2 matrix: "))

    print("Matrix 1: ")
    m1 = input_matrix(r1, c1)

    print("Matrix 2: ")
    m2 = input_matrix(r2, c2)

    print("Matrix 1: ")
    print(m1)

    print("Matrix 2: ")
    print(m2)

    if c1 != r2:
        print("It isn't possible to make any multiplication, rows and columns must be equal")
        return

    print("Add")
    print(adding_matrix(m1, m2))

    print("Substract")
    print(subtract_matrix(m1, m2))

    print("Multiple")
    print(multiple_matrix(m1, m2))

    print("Divide")
    print(divide_matrix(m1, m2))


if __name__ == "__main__":
    program()
