n, m = map(int, input().split())
matrix, arr = [], []
maximal, row, counter = 0, 0, 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for x in range(n):
    for y in range(m):
        if matrix[x][y] > maximal:
            maximal = matrix[x][y]
            row = x

for j in range(len(matrix)):
    if maximal in matrix[j]:
        counter += 1
        continue

print(counter)

# The program receives as input two numbers 'n' and 'm', which are the number of rows
# and columns in the array. Next, the input stream contains
# 'n' lines of 'm' numbers each, which are elements of the array.

# The program determines the number of rows in the array
# that contain the value equal to the largest.