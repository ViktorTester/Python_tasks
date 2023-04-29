n = list(input())
a = set(n)

if len(n) == len(a):
    print('NO')
else:
    for i in a:
        if i in n:
            n.remove(i)

    arr = [int(j) for j in n if j.isdigit()]

    print(*sorted(set(arr)))

# The program outputs in ascending order all the digits
# that occur more than once in a character string.