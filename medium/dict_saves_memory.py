def f(x):
    return x + 3


d = {}

for i in range(int(input())):
    n = int(input())
    if n not in d.keys():
        d[n] = f(n)
        print(f(n))
    else:
        for key, value in d.items():
            if n == key:
                print(value)

# The program reads a line with the number 'n', which specifies
# the number of numbers to be read. Further reads
# 'n' lines with numbers, one number 'i' in each line.
# There will be n + 1 lines in total.

# When reading a number, the program outputs the value f(x[i]) on a separate line.

# The function is calculated long enough and depends only on the passed argument i.