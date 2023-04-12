matrix = []
position = 0

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == 1:
            position = abs(2 - r) + abs(2 - c)

print(position)

# The input is a matrix of size 5x5, consisting of 24-x zeros and a single 1.
# The program calculates the minimum number of steps from 1 to the center
# of the matrix. In one move, it is allowed to apply one of
# the following two transformations to the matrix:

# Swap two adjacent rows of the matrix, i.e. rows with numbers i and i + 1.
# Swap two adjacent columns of the matrix, that is, columns with numbers j and j + 1.