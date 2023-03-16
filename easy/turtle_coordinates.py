coords = [input().split() for j in range(int(input()))]
turtle = [0, 0]

for i in range(len(coords)):
    if coords[i][0] == 'north':
        turtle[1] += int(coords[i][1])
    elif coords[i][0] == 'south':
        turtle[1] -= int(coords[i][1])
    elif coords[i][0] == 'west':
        turtle[0] -= int(coords[i][1])
    elif coords[i][0] == 'east':
        turtle[0] += int(coords[i][1])

print(*turtle)

# The turtle moves according to the format command (north 20, south 30, and so on).

# The program is given as input the number of commands 'n' that the turtle needs
# to execute, after which 'n' lines with the commands themselves. The program
# prints two numbers on one line: the first and second
# coordinates of the turtle's end point. All coordinates are integer.