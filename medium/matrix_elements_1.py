n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)

for r in range(n):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

# The program takes as input a natural number N - the number of rows and columns
# of the matrix. Each of the following N lines contains N integers – matrix elements.

# The program goes through the elements of this matrix from top to bottom from left
# to right and displays the elements in that order in the form of a table.

