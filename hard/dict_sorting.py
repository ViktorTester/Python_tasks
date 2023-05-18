d = {}
arr = []
for i in range(int(input())):
    data = input().split(maxsplit=1)
    data[1] = data[1][-3:]
    if data[1] not in d.keys():
        d[data[1]] = [data[0]]
    else:
        d[data[1]] += [data[0]]

for j in range(int(input())):
    name = input()
    if name in d.keys():
        for key, value in d.items():
            if key == name:
                print(*sorted(value))
    else:
        print('No data')

# John has N classmates. John couldn't remember their birthdays and decided to make
# a calendar of class birthdays. The program determines who has a birthday in a given month.

# Input Format
# The first line contains an integer N — the number of John's classmates.
# The next N lines contain information about their birthdays.
# Each line consists of three parts, separated by a space - the name of a
# classmate, the day and month of his birth. The name is a string of english
# letters, the day is a number from 1 to 31, and the month is a string from the
# set Jan, Feb, Mar, Apr, May, Jun, Jul, "Aug", "Sep", "Oct", "Nov", "Dec".

# The names of all John's classmates are different.
# The next line contains an integer M — the number of questions to be answered.
# The next M lines contain the questions themselves.
# The question is the name of the month in the same format as they are given above.

# Output Format
# For each question, in a separate line separated by a space, the program displays
# the names of all classmates who were born in the specified month.
# The names are ordered in lexicographic order.

# If no one was born in the given month, the message "No data" will be displayed.
