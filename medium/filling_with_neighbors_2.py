n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

# Given a rectangular matrix of size NxM, in which values are filled only in
# the last column and in the last row. All other elements are zero and are considered empty.
#
# The program fills in each empty element by adding the neighbor on the right and
# the neighbor on the bottom, starting with those elements for which both
# specified neighbors are filled (not equal to zero).