tasks, home = map(int, input().split())
mins = 240 - home
counter = 0

while mins >= 5 * (counter + 1) and counter < tasks:
    mins -= 5 * (counter + 1)
    counter += 1

print(counter)

# The student started solving tasks at 20:00. There are 'n' tasks ordered by
# increasing difficulty, i.e. task 1 will be the easiest, and task number 'n' will
# be the most difficult. The student will need 5 · 'i' minutes to solve the i-th problem.

# However, the student wants to be in time for a movie
# screening at the cinema that starts at 24:00.

# The program determines how many maximum tasks the student
# can solve without being late for the session.
#
# The first line of the input contains two integers 'n' and 'k' — the number of tasks
# and the number of minutes it takes the student to get from home to the cinema.