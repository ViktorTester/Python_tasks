dct = {}

for i in range(int(input())):
    name = input()
    if name in dct:
        print(f'{name}{dct[name]}')
        dct[name] += 1
    else:
        print('OK')
        dct[name] = 1

# Every time a new user wants to register, he sends a 'name' request to the system
# with his name. If this name is not contained in the system database, then it is
# entered there and an 'OK' response is returned to the user, confirming successful
# registration. If there is already a user with the name 'name' on the site,
# then the system generates a new 'name' and gives it to the user as a hint, while
# the hint is also added to the database. The new 'name' is formed according to
# the following rule: numbers are sequentially assigned to name, starting from one
# (name1, name2, ...), and among them the smallest 'i' is found such that
# name'i' is not contained in the site database.