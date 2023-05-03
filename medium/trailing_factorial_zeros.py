def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n, counter=0):
    for i in reversed(str(factorial(n))):
        if i == '0':
            counter += 1
        else:
            return counter
    return counter


assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Correct')