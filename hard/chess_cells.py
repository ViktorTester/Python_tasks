one, two = input(), input()
s = 'abcdefgh'
a = s.find(one[0])
b = int(one[1])
c = s.find(two[0])
d = int(two[1])
if ((a + b) % 2 == 0 and (c + d) % 2 == 0) or ((a + b) % 2 == 1 and (c + d) % 2 == 1):
    print("YES")
else:
    print("NO")

# The program receives the coordinates of two cells of the chessboard as input and
# displays a message about whether these cells are of the same color.
# The columns on the chessboard are indicated by lowercase English letters.