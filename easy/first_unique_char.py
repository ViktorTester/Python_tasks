def first_unique_char(s):
    for index, value in enumerate(s):
        num = s.count(value)
        if num == 1:
            return index
    return -1


s = input()
print(first_unique_char(s))

# The first_unique_char function takes a string of characters and returns
# an integer: the position of the first unique character in the string.
# If there are no unique characters, -1 is returned.
# Characters are case-insensitive.
