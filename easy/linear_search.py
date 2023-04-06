s = input().split()
a = input()

for i in range(len(s)):
    if a in s[i]:
        print(i + 1)
        break
else:
    print('ErrorValue')

# The program receives as input in one line the elements of the list - integers
# separated by a space. The number of elements is arbitrary.

# And on the next line, one number r is entered - the value of the search.

# The program implements a linear search algorithm for the entered value r.