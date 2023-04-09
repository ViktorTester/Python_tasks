n = int(input())
counter = 0
total = 0

for i in range(n + 1, 2 * n):
    counter = 0
    for j in range(2, round(n * 0.5) + 1):
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        total += 1

print(total)

# Bertrand's postulate says that for any n > 1 there is a prime
# number 'p' in the interval n < p < 2n.

# Number 'n' is given. The program finds the number of primes 'p' from the interval n < p < 2n.

# A number is called prime if it is only divisible by itself and one.
