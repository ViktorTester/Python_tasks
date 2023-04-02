list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

total = list1 + list2
arr = []

while len(total) != 0:
    item = min(total)
    total.remove(item)
    arr.append(item)

print(*arr)

# The input to the program is two strings of numbers, each on a separate line.
# The program merges them into one sorted list in ascending
# order without using the built-in sorting methods