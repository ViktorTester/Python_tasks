a, b, c = int(input()), int(input()), int(input())

x1 = a + b + c
x2 = a * b * c
x3 = (a + b) * c
x4 = a * (b + c)

print(max(x1, x2, x3, x4))

# There are three positive integers a, b, c. The program places '+' and '*' operator
# signs between these numbers, and, possibly, parentheses. The value of the
# resulting expression should be as large as possible.

# The program uses only the built-in standard methods for working
# with variables: max(), min(), int(), float(), sum()