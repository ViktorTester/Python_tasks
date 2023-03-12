def update_dictionary(d, key, value):
    if key not in d.keys():
        if key * 2 not in d.keys():
            d[key * 2] = [value]
        else:
            d[key * 2] += [value]
    elif key in d.keys():
        d[key] += [value]


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)

# The update_dictionary(d, key, value) function takes a dictionary 'd'
# and two numbers as input: 'key' and 'value'.

# If the 'key' key is in the d dictionary, then the
# 'value' value is added to the list stored by this key.

# If the 'key' key is not in the dictionary, the value is added to the list by the key 2 ∗ 'key'.

# If there is no key 2 ∗ 'key' either, then the key 2 ∗ 'key' is added to
# the dictionary and the list from the passed [value] element is compared to it.