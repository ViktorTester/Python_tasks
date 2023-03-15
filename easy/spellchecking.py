words = [input().lower() for i in range(int(input()))]
texts = [input().lower().split() for j in range(int(input()))]

wrong = set()
for i in range(len(texts)):
    for j in range(len(texts[i])):
        if texts[i][j] not in words:
            wrong.add(texts[i][j])

print(*wrong, sep='\n')

# The simplest spell checker can be based on a list of known words.
# If the entered word is not found in this list, it is marked as "error".

# The number 'd' of words known to us is passed to the input of the program
# in the first line, after which these words are indicated on 'd' lines.
# Then the number 'l' of lines of text to check is passed, after which 'l' lines of text.

# The program displays unique "errors" in random order, case-insensitive.