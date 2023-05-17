d = {}
for i in range(int(input())):
    winners = input()
    d[winners] = d.get(winners, 0) + 1

d = sorted(d.items(), key=lambda x: -x[1])
print(*d[0], sep=', ')
print(*d[-1], sep=', ')

# The program takes as input in the first line a natural number 'n' - the number
# of awards to be given. And then in the next 'n' lines enter
# the names of the athletes - the winners.

# The program displays in separate lines the names of the athletes with the highest
# and lowest number of awards and their number separated by commas. It is guaranteed
# that there will always be only one person with the highest and lowest number of figurines.