def print_goods(*args):
    arr = []
    for i in args:
        if type(i) == str and len(i) > 0:
            arr.append(i)

    if len(arr) > 0:
        for index, value in enumerate(arr, 1):
            print(f'{index}. {value}')
    else:
        print('Empty')

# The print_goods function, which prints the shopping list. It accepts an arbitrary
# number of values as input, and any non-empty strings are considered a product.
# Numbers, lists, dictionaries, and other non-string objects are ignored.