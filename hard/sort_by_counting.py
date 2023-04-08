a = map(int, input().split())
count = [0] * 201

for i in a:
    count[i] += 1

for i in range(-100, 101):
    for _ in range(count[i]):
        print(i, end=' ')

# The program sorts a list consisting only of numbers
# between -100 and 100 inclusive, by counting sort.

# The program receives as input the elements of the list in one line separated by a space.
