with open('words.txt', encoding='utf-8') as file:
    text = file.read().lower().split()

    result = {}
    for x in text:
        result[x] = result.get(x, 0) + 1

    print(result)

    max_value = 0
    for key, value in result.items():
        if max_value < value:
            max_value = value
            frequent_word = key

print(frequent_word, max_value)

# The program reads the text from the file (there can be more than one line in the file)
# and displays the most frequent word in this text and, separated by a space,
# how many times it occurred. If there are several such words,
# output the first one lexicographically.

# Words written in different registers are considered the same.
