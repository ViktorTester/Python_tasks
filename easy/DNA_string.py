s = input()
dna = s[0]
count = 0

for i in range(1, len(s)):
    count += 1
    if dna[-1] != s[i]:
        dna += str(count)
        dna += s[i]
        count = 0
dna = dna + str(count + 1)

print(dna)


# The program compresses repeated characters in a DNA string.
# Groups of identical characters in the original string are replaced with that
# character and the number of times it occurs at that position in the string.