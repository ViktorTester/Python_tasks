persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

arr, arr2 = [], []

for i in persons:
    arr.append(i[0])
    arr2.append(dict(salary=i[1], gender=i[2], passport=i[3]))

data = dict(zip(arr, arr2))

# Based on the persons variable, which stores a list of tuples, each tuple stores
# the person's name, salary, gender, and passport, the program creates a dictionary
# where the keys are names, and the values are a dictionary
# of three keys: salary, gender, and passport