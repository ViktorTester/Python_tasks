S = input()
S = int(S)

D_1 = S // 100000
D_2 = S // 10000 % 10
D_3 = S // 1000 % 10
D_4 = S // 100 % 10
D_5 = S // 10 % 10
D_6 = S % 10

if D_1 + D_2 + D_3 == D_3 + D_4 + D_5:
    print('Lucky')
else:
    print('Common')

# The program finds out if the ticket is lucky.
# The input to the program is a string of six digits.
# A ticket is considered lucky if the sum of the first three digits matches
# the sum of the last three digits of the ticket number.

# version 2
n = list(map(int, list(input().zfill(6))))
if n[0] + n[1] + n[2] == n[-1] + n[-2] + n[-3]:
    print('YES')
else:
    print('NO')