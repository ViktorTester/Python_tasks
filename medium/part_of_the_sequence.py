n = int(input())

arr = [i * [i] for i in range(1, n + 1)]

nums = [num for group in arr for num in group]

print(*nums[:n])

# The program displays part of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (the number is repeated as many times as it is equal to). A non-negative integer
# n is passed to the input of the program — this is how
# many elements of the sequence the program displays.