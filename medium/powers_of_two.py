n = int(input())
s = 0
counter = 0
while s < n:
    s = 2 ** counter
    counter += 1
if s == n:
    print(counter - 1)
else:
    print('NO')

# Numbers that are powers of two play an important role in computer architecture:
# 1, 2, 4, 8, and so on. The program checks if the entered natural number is a power
# of two. If yes, then this degree itself is displayed; if not, displays "NO"