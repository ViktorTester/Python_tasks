n = input()

if len(n) == 2:
    print(0)
else:
    n = set(n[1:-1].split(', '))
    print(len(n))

# The first and only line contains a description of the set of letters.
# It is guaranteed that the string starts with an opening brace and ends
# with a closing brace. Small Latin letters are listed between them
# separated by commas. Each comma is followed by a space.

# The program displays the number of different letters in the set.