total = 1
arr = []

while True:
    n = int(input())
    total += n
    arr.append(n ** 2)
    if total - 1 == 0:
        print(sum(arr))
        break


# The program reads numbers from the console (one per line) until the
# sum of the entered numbers is 0 and immediately after that displays
# the sum of the squares of all the numbers read.