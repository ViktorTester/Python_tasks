a = map(int, list(input()))
count = [0] * 10

for i in a:
    count[i] += 1

for i in range(10):
    if count[i] > 0:
        print(i, count[i])

# The input to the program is a positive integer 'n'.
# The program displays in ascending order all the digits that occurred in this
# number, and lso how many times this digit occurred in the number 'n'