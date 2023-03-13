with open('dataset.txt', encoding='utf-8') as file1, open(
        'answer.txt', 'w', encoding='utf-8') as file2:
    TEXT = file1.read()

    ARR = []
    S = ''

    for i in range(len(TEXT)):
        if TEXT[i].isalpha():
            ARR.append(TEXT[i])
            if S != '':
                S += ','
        elif TEXT[i].isdigit():
            S += TEXT[i]

    S = S.split(',')
    ANSWER = ''

    for i in range(len(S)):
        ANSWER += ARR[i] * int(S[i])

    print(ANSWER, file=file2)

# The program reads from the file a line corresponding to the text compressed
# using repetition coding and performs the reverse operation, obtaining the original text.