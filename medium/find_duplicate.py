def find_duplicate(lst):
    arr = []
    for i in lst:
        num = lst.count(i)
        if num > 1 and i not in arr:
            arr.append(i)
        else:
            continue
    return arr


assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Correct')

# The find_duplicate function takes one argument, a list of numbers.
# The function returns a list of duplicates, each duplicate is taken only once
# in the order in which they occur in the original list.
# A double is a number that was present in the list several times.
