n = int(input())
hours = n // 60 // 60
minutes = n // 60 - (hours * 60)
seconds = n % 60

print(hours, str(minutes // 10) + str(minutes % 10), str(seconds // 10) + str(seconds % 10), sep=':')

# Electronic clocks show the time in the format h:mm:ss, first the number of hours
# is written in the range from 0 to 23, then the two-digit number of minutes,
# then the two-digit number of seconds. The number of minutes and seconds are padded
# to a two-digit number with zeros, if necessary.

# The program takes as input the number n - the number of seconds that have passed
# since the beginning of the day and displays the clock, observing the format.
