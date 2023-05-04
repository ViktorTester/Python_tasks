def first_repeated_word(n: str) -> str or None:
    """Finds the first duplicate in a string"""
    n = n.split()
    arr = []
    for i in n:
        if i not in arr:
            arr.append(i)
        else:
            return i
    return None


assert first_repeated_word("ab ca bc ab") == "ab"
assert first_repeated_word("ab ca bc Ab cA aB bc") == "bc"
assert first_repeated_word("ab ca bc ca ab bc") == "ca"
assert first_repeated_word("ab ca bc") is None
print('Correct')

# The first_repeated_word function takes a string consisting of several words,
# the words are separated by a space. The function finds the first repeated word
# and returns it as a result. If a string is passed in which all words are different,
# the function returns 'None'
