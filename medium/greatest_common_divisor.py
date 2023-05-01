def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


arr = [int(input()) for _ in range(int(input()))]
total = arr[0]

for i in arr:
    total = gcd(total, i)

print(total)

# The first line contains a natural number n, the number of numbers.
# Next come n lines, each containing a natural number.

# The program prints out the greatest common divisor of these numbers.