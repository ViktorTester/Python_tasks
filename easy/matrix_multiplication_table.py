n, m = map(int, input().split())
matrix = []
counter = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == m:
            counter += 1

print(counter)

# Consider a table with n rows and n columns. It is known that the cell formed by the
# intersection of the i-th row and the j-th column contains the number i×j.
# Rows and columns are numbered starting from one.

# The input in one line is the numbers n and x — the size of the table and the
# number that the program is looking for in the table.

# The program counts the number of cells in the table containing the number x.