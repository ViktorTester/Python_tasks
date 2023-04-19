import sys

n, m = map(int, input().split())
matrix = []
flag = True

for x in range(n):
    matrix.append(input().split())
    for y in range(m):
        if matrix[x][y] in 'CMY':
            flag = False
            print('#Color')
            sys.exit()
if flag:
    print('#Black&White')

# The photo is an n×m matrix, each cell of which contains a symbol indicating the
# color of the corresponding pixel. There are 6 colors in total:

# 'C' (cyan)
# 'M' (magenta)
# 'Y' (yellow)
# 'W' (white)
# 'G' (grey)
# 'B' (black)

# A photo can be considered black and white if it contains only white, gray, or black.
# If there is at least one pixel of cyan, magenta or yellow, it is colored.