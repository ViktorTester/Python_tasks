n, m = map(int, input().split())
matrix = []

maximal, col, row = 0, 0, 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for x in range(n):
    for y in range(m):
        if matrix[x][y] > maximal:
            maximal = matrix[x][y]
            row = x
            col = y

print(maximal)
print(row, col)

# The program receives as input two numbers 'n' and 'm', which are the number of rows
# and columns in the array. Next, the input stream contains 'n' lines of 'm'
# numbers each, which are elements of the array.

# The program prints the value of the maximum element, followed by
# the row number and the column number in which it occurs.