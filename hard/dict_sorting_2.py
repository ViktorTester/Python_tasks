d = {}
while True:
    data = input().split(',')
    if data == ['end']:
        break
    else:
        if data[0] not in d.keys():
            d[data[0]] = [int(data[1])]
        else:
            d[data[0]] += [int(data[1])]

for key, value in sorted(d.items(), key = lambda x: (-(sum(x[1]) / len(x[1])), x[0])):
    print(key, sum(value) / len(value))

# The head of the taxi fleet wants to see a report on all taxi drivers, where you
# need to indicate the name of the taxi driver and his average rating.
# The information in the report should be arranged in descending order
# of the average rating of the taxi driver.

# After each successfully completed order, the client gives the taxi driver
# a rating - an integer from 1 to 5.

# Input data
# The program accepts lines that first indicate the name of the taxi driver, and then,
# separated by a comma with a space, his rating for the order.

# The line "end" is the last line and means the end of the input

# Output
# The taxi drivers are listed in descending order of their average rating, and the
# program prints each taxi driver's name and average rating on a separate line.
# In the event of a match in the average ratings, each group of taxi drivers with
# the same rating is located by name in alphabetical order