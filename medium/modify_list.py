def modify_list(l):
    for i in reversed(range(len(l))):
        if l[i] % 2 == 1:
            l.remove(l[i])
        else:
            l[i] = int(l[i] / 2)


lst = [1, 2, 3, 4, 5, 6]

print(lst)

# The modify_list(l) function takes a list of integers as input, removes all
# odd values from it, and divides the even ones by two. The function does not
# return anything, it only modifies the passed list.
