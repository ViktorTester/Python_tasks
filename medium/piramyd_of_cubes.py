n = int(input())
a, b, = 0, 0
counter = 0

while n >= 0:
    a += 1
    b += a
    n -= b
    counter += 1

print(counter - 1)

# The boy has n cubes. He decided to build a pyramid out of them. The pyramid is built
# as follows: at the top of the pyramid there should be 1 cube, at the second
# level - 1 + 2 = 3 cubes, at the third level - 1 + 2 + 3 = 6 cubes, and so on.
# Thus, at the i-th level of the pyramid there should be 1 + 2 + ... + (i - 1) + i cubes.

# The first line contains an integer n - the number of cubes the boy initially has.