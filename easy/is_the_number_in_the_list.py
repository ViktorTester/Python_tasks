lst = input().split()
x = input()

arr = [i for i in range(len(lst)) if lst[i] in x]

if len(arr) == 0:
    print('Отсутствует')
else:
    print(*arr)


# The program reads a list of numbers lst from the first line and a number 'x'
# from the second line and displays all the positions
# where the number 'x' occurs in the given list lst.

# Positions are numbered from zero

# If the number x is not found in the list, the string "Missing" is displayed.

# Positions are displayed in one line, in ascending order of absolute value.
