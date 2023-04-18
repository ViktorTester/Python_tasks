n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

# Given a rectangular matrix of size NxM, in which values are filled
# only in the first column and in the first row. All other elements
# are zero and are considered empty.

# The program fills each empty element by adding the neighbor on the left
# and the neighbor on the top, starting with those elements for
# which both specified neighbors are filled (not equal to zero).