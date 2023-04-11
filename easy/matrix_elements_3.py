a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(list(map(int, input().split())))
    arr[i].reverse()
    print(*arr[i])

# The program takes as input two natural numbers N and M - the number of rows
# and columns of the matrix. Each of the next N lines contains M integers – matrix elements.
#
# The program displays the elements of the matrix from right
# to left from top to bottom in the form of a table.