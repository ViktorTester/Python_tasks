matrix, arr = [], []

for _ in range(n := int(input())):
    matrix.append([0] * n)

a, b, c = map(int, input().split())

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = c
        elif i < j:
            matrix[i][j] = a
        else:
            matrix[i][j] = b

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()

# The program first takes as input the number N - the number of rows and columns
# in the matrix, and then on a new line three integers A, B and C.
# Then the matrix is filled:

# all elements above the main diagonal are filled with the value A;

# all elements below the main diagonal are filled with the value B;

# all elements on the main diagonal are filled with the value C.