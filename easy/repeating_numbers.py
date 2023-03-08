s = input().split()

arr = []
arr2 = []

for i in range(len(s)):
    if s[i] in arr:
        if s[i] not in arr2:
            arr2.append(s[i])
        else:
            continue
    else:
        arr.append(s[i])

print(*arr2)


# The program takes as input a list of numbers in one line and displays
# in one line the values that occur in it more than once.
# The output numbers are not repeated, the order of their output is arbitrary.