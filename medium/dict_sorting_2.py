d = {}
while True:
    item = input().split(':')
    if item == ['end']:
        break
    else:
        d[item[0]] = int(item[1])

for key, value in sorted(d.items(), key=lambda x: -x[1]):
    print(key)

# The program accepts strings in which the name of the product is indicated first,
# and then, separated by a colon with a space, its price is a positive integer.

# The line "end" means the end of the list of goods and, accordingly, the end of the input

# All products have unique names, prices are not duplicated.
#
# The program displays a list of products by decreasing price