a, b, c, d = int(input()), int(input()), int(input()), int(input())
p = '\t'

for i in range(a, b + 1):
    s = str(i) + '\t'
    for j in range(c, d + 1):
        p += str(j) + '\t'
        s += str(i * j) + '\t'
    if len(p) < len(s):
        print(p)
    print(s)

# The input is four numbers a, b, c and d, each in its own line.
# The program displays a fragment of the multiplication table for all numbers
# in the interval [a; b] to all numbers of the interval [c; d].