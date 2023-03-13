with open('grades.txt', encoding='utf-8') as file1, open(
        'answer.txt', 'w', encoding='utf-8') as file2:
    text = [line.strip().split(';') for line in file1.readlines()]

    ln1, ln2, ln3 = 0, 0, 0

    for i in range(len(text)):
        avg = 0
        ln1 += int(text[i][1])
        ln2 += int(text[i][2])
        ln3 += int(text[i][3])
        for j in range(1, len(text[i])):
            avg += int(text[i][j])
        print(avg / 3, file=file2)

    print(ln1 / len(text), ln2 / len(text), ln3 / len(text), file=file2)

# There is a file with data on the progress of students. It is a set of lines,
# where each line contains the following information:
# Surname;Math_grade;Physics_grade;Chemistry_grade
#
# Fields within a row are separated by semicolons, scores are integers.

# The program reads a source file with a similar structure and for each student
# writes his average mark in three subjects on a separate line corresponding
# to this student in the file with the answer.

# The program also calculates the average scores in mathematics,
# physics and chemistry among all students and adds the resulting values,
# separated by a space, to the last line in the answer file.
