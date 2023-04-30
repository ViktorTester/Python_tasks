card = list((map(int, input())))
arr = []

for index, value in enumerate(card, 1):
    if index % 2 == 0:
        arr.append(value)
    else:
        value *= 2
        if len(str(value)) > 1:
            value -= 9
            arr.append(value)
        else:
            arr.append(value)
            continue

print(sum(arr) % 10 == 0)

# The sum of certain numbers on the map must pass the conditions of the Luhn algorithm.
# A simplified version of the algorithm looks like this:

# The digits of the sequence to be checked are numbered from right to left.

# Numbers in odd places remain unchanged.

# Numbers in even places are multiplied by 2.

# If such a multiplication results in a number greater than 9, it is reduced by the value 9

# All 16 digits obtained as a result of the conversion are added up.
# If the sum is a multiple of 10, then the original data is correct.