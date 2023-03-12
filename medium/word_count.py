keys = input().lower().split()

values = [keys.count(keys[j]) for j in range(len(keys))]

d = dict(zip(keys, values))

for key, value in d.items():
    print(key, value)

# The program reads one line from standard input and outputs for each unique
# word on that line the number of times it occurs (case-insensitive).
# Each unique word is displayed only once.