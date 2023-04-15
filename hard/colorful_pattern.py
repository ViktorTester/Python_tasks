matrix = [list(input()) for _ in range(4)]

n = len(matrix)
flag = True

for r in range(n - 1):
    for c in range(n - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            print('No')
            flag = False
            break
if flag:
    print('Yes')

# The program receives 4 lines as input, 4 characters "W" or "B" in each,
# describing the pattern of tiles. The symbol "W" stands for white tiles, and "B" for black.

# A suitable pattern is one that does not contain
# a 2x2 square consisting of tiles of the same color.

# The program outputs "Yes" if the pattern is suitable and "No" otherwise.