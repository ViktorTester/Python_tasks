n = list(map(int, input().split()))
my_dict = {}
d = n.pop()

while len(n) > 0:
    d = {n.pop(): d}

print(d)

# The program converts a list of integers of arbitrary length into
# a dictionary whose nesting depends on the length of the list.