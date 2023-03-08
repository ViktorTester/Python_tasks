figure = input()
if figure == 'triangle':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif figure == 'rectangle':
    a, b = int(input()), int(input())
    print(a * b)
else:
    r = int(input())
    print(3.14 * (r ** 2))


# The program finds the areas of some figures.
# The input is the shape type (triangle, rectangle and circle)
# and the corresponding parameters.