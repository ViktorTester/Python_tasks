matrix, arr = [], []

for _ in range(n := int(input())):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i + j == len(matrix) - 1:
            arr.append(matrix[i][j])

print(max(arr))

# The program first takes the number N as input - the number of rows and columns
# in the list, and then the elements of the list are written in 'N' lines and displays
# the largest element on the secondary diagonal.