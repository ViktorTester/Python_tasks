n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)

# The program receives as input the number 'n' - the number of elements
# in the list, and then the list itself in the next line.

# The program sorts the list in ascending order using insertion sort.