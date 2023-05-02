def format_name_list(names: list):
    arr = []
    for i in names:
        for value in i.values():
            arr.append(value)

    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return ''
    elif len(arr) == 2:
        return arr[0] + ' and ' + arr[1]
    else:
        arr = ', '.join(arr[:-2]) + ', ' + arr[-2] + ' and ' + arr[-1]
        return arr


assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
                         {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer and Marge'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa and Maggie'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart and Lisa'

assert format_name_list([{'name': 'Bart'}]) == 'Bart'

assert format_name_list([]) == ''

print('Correct')

# The format_name_list function takes a list of dictionaries,
# each dictionary in this list has only the 'name' key.

# The format_name_list function returns a string in which all names from the
# list are separated by a comma except the last two names,
# they are separated by the union 'and'.
# If there is no name in the list, the function returns an empty string.
