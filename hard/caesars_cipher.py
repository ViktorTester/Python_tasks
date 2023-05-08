def shift_letter(letter: str, shift: int) -> str:
    """The function shifts the character letter by shift positions"""

    return chr((ord(letter) - 97 + shift) % 26 + 97)

def caesar_cipher(text: str, shift: int) -> str:
    """Caesar's cipher"""
    words = []
    for word in text.split():
        new_word = ''

        for char in word:
            if char.isalpha():
                new_word += shift_letter(char, shift)
            else:
                new_word += char
        words.append(new_word)

    return ' '.join(words)

print(caesar_cipher(input(), int(input())))

# The caesar_cipher function takes text and an offset value as input.

# Inside the caesar_cipher function, the program goes through each character
# sequentially and converts it according to the following rules:

# if the character is a punctuation mark, it is left as is
# if it is a letter, then it shifts it using the shift_letter function:


# The shift_letter function takes two arguments:

# letter - one lowercase English letter
# shift - integer value of letter shift (can be either positive or negative)