n, m = map(int, input().split())
matrix = []
total = 0
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    arr.append(sum(matrix[i]))

print(a := max(arr), arr.index(a), sep = '\n')

# The program receives as input two numbers 'n' and 'm', which are the number of rows
# and columns in the array. Next, the input stream contains
# 'n' lines of 'm' numbers each, which are elements of the array.

# The program displays 2 numbers: the amount and the number of the line for
# which this amount is reached. If there are several such lines,
# then the number of the smallest of them is displayed.