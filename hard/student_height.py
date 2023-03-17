with open('students', encoding='utf-8') as file:
    d = {}
    text = [line.split() for line in file.readlines()]

    for i in text:
        i[0] = int(i[0])
        i[2] = int(i[2])

    for j in text:
        if j[0] in d:
            d[j[0]].append(j[2])
        else:
            d[j[0]] = [j[2]]

    for k in sorted(d.keys()):
        print(k, '', sum(d[k]) / float(len(d[k])))

# A file with a table in TSV format with information about the
# height of schoolchildren of different classes is given.

# The program reads this file and calculates the average student height for each class.

# The file consists of a set of lines, each of which represents three fields:
# Class Surname Height

# The class is indicated only by a number. Letter modifiers are not used.
# The class number can be from 1 to 11 inclusive. There are no spaces in the surname,
# and a natural number is used as growth, but when calculating
# the average, the program calculates the value as a real number.

# Information about the average height is displayed in ascending order
# of the class number (for classes from the first to the eleventh).