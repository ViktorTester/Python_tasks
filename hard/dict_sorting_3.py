friends = {}
names = ['John', 'Bob', 'Sean']

while True:
    line = input()
    if line == "конец":
        break

    boy, commenter = line.split(': ')

    if boy not in friends:
        friends[boy] = set()

    friends[boy].add(commenter)

for i in names:
    if i not in friends.keys():
        friends[i] = []

sorted_friends = sorted(friends.items(), key=lambda x: len(x[1]), reverse=True)
for boy, commenters in sorted_friends[:3]:
    print(f'{boy} has {len(commenters)} unique commenters')

# Three friends have social media accounts. Their pages became popular and, of course,
# there were fans leaving comments. The guys decided to find out which of them has
# the largest number of unique commentators.

# Input data
# Each line will contain one of the friends' names, followed by a colon and a space,
# the commenter's name. Commentators can repeat and comment on different characters

# The string "end" means the end of the input and occurs last

# Input data
# The program outputs in descending order of popularity 3 lines with the names of
# friends and the number of unique commenters.