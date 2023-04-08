total = 0
arr = []
for i in range(1000, 10000):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    if s == 20:
        total += i
print(total)

# The program finds the sum of all four-digit natural numbers whose sum of digits is 20.