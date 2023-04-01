n = input()

while int(n[0]) != 1 and int(n) < 10 * 10 ** 8:
    n = str(int(n[0]) * int(n))

print(n)

# The input to the program is a number. It is multiplied by its own first digit.
# The result is multiplied by the first digit of the result. And so on.
# The program determines what number will be the result until the first digit of
# the resulting number becomes equal to 1, or until it exceeds a billion.