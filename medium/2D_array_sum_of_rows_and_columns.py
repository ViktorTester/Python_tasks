n, m = map(int, input().split())
matrix = []
total = 0
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    arr.append(sum(matrix[i]))

print(*arr)

for r in range(m):
    total = 0
    for c in range(n):
        total += matrix[c][r]
    print(total, end=' ')


# The input is an integer two-dimensional array consisting of N rows and M columns.
# The program calculates the sum of the elements in each row and in each column.