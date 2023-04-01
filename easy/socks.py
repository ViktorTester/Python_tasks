n, m = map(int, input().split())
counter = 1

while n > 1:
    n -= 1
    counter += 1
    if counter % m == 0:
        n += 1

print(counter)

# The boy has 'n' pairs of socks. In the morning every day, going to school,
# the boy must put on a pair of socks. In the evening, after coming home from school,
# the boy takes off his socks and throws them away. Every 'm'-th day the mother buys
# one pair of socks for the boy. She does this late at night, so the boy can't put
# on new socks until the next day. How many days in a row will the boy have enough socks?