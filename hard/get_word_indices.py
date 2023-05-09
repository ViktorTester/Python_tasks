def get_word_indices(strings: list[str]) -> dict:
    d = {}
    for i in range(len(strings)):
        for j in strings[i].lower().split():
            if j not in d:
                d[j] = [i]
            else:
                d[j].append(i)
    return d

# The get_word_indices function takes a list of strings and returns a dictionary,
# where keys are unique lowercase words from a list of strings, and values are lists
# of string indices in which those words occur.