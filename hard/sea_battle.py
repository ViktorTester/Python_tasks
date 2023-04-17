a, b = map(int, input().split())
M = ['.' * (b + 2)]
counter = 0

for _ in range(a):
    M.append('.' + input() + '.')

M.append('.' * (b + 2))

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if M[i + 1][j] == '.' and M[i - 1][j] == '.' and M[i][j + 1] == '.' and M[i][j - 1] == '.' and M[i][j] == '.':
            counter += 1

print(counter)

# The program reads two numbers: 'a' and 'b' . The next a lines describe the playing
# field - each line contains 'b' characters. The symbol "." (dot) indicates a free cell,
# the symbol "*" (star) - occupied by the ship.

# The program displays the number of ways to put a single-deck ship on the field.
# According to the rules, it can only be placed in that cell, all adjacent to which
# are not occupied. In this problem, cells that have a common side are considered neighbors.
