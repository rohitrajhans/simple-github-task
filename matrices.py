from numpy import empty
from numpy import zeros
import numpy as np


# m1rows
m = int(input("Enter the number of rows in matrix 1 : "))
# m1cols
n = int(input("Enter the number of cols in matrix 1 : "))

# m2rows
r = int(input("Enter the number of rows in matrix 2 : "))
# m2cols
s = int(input("Enter the number of cols in matrix 2 : "))

mat1 = empty([m, n])
mat2 = empty([r, s])


if n == r:
    print("Matrices are compatible for multiplication")
    result = zeros([m, s])
    print("Please enter the Matrix 1:")
    for x in range(0, m):
        for y in range(0, n):
            mat1[x][y] = input()

    print("Please enter Matrix 2: ")

    for a in range(0, r):
        for b in range(0,s):
            mat2[a][b] = input()

    '''  for i in range(0, m):
        for j in range(0, s):
            for k in range(0, r):
                result[i][j] += mat1[i][k] * mat2[k][j]'''
    result = np.dot(mat1,mat2)

    print("Matrix 1")
    for p in mat1:
        print(p)

    print("Matrix 2")
    for p in mat2:
        print(p)


    print()
    print("Product matrix :")

    for p in result:
        print(p)


else:
    print("Matrices are not compatible for multiplication!")
