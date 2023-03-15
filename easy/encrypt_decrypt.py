sym, code_sym = list(input()), list(input())
to_encrypt, to_decrypt = input(), input()

d = dict(zip(sym, code_sym))

enc = ''
for i in range(len(to_encrypt)):
    for key, value in d.items():
        if to_encrypt[i] in key:
            enc += value

dec = ''
for i in range(len(to_decrypt)):
    for key, value in d.items():
        if to_decrypt[i] in value:
            dec += key

print(enc)
print(dec)

# The program can encrypt and decrypt the substitution cipher. The program takes
# two strings of the same length as input, the first line contains the characters
# of the source alphabet, the second line contains the characters of the final
# alphabet, after which there is a string that needs to be encrypted with the passed
# key, and another line that needs to be decrypted.