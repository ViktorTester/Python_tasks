def shift_letter(letter: str, shift: int) -> str:
    """The function shifts the character 'letter' by 'shift' positions"""

    return chr((ord(letter) - 97 + shift) % 26 + 97)


assert shift_letter('b', 2) == 'd'
assert shift_letter('d', 1) == 'e'
assert shift_letter('z', 1) == 'a'
assert shift_letter('d', -2) == 'b'
assert shift_letter('d', 26) == 'd'
assert shift_letter('b', -3) == 'y'
print('Correct')

# The shift_letter function takes two arguments:

# letter - one lowercase English letter
# shift - integer value of letter shift (can be either positive or negative)
