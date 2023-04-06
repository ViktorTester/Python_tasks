s = input()
counter = 0
x = len(s)

while x != 0:
    if s[counter] not in 'ea':
        print(f'Current letter is: {s[counter]}')
        counter +=1
        x -= 1
    else:
        print('Aha! Found')
        break
if x == 0:
    print('All letters printed')

# The input is a word and the program, in a while loop,
# goes through all its letters and prints them out.

# As soon as the lowercase English letters "e" or "a" come across, the program
# displays the phrase "Aha! Found”, stops typing letters and forcibly exits the loop.