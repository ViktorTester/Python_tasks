def calculate(x: float, y: float, operation: str = 'a'):
    """basic calculator but created with a nested functions"""

    def addition():
        print(float(x + y))

    def subtraction():
        print(float(x - y))

    def division():
        print(float(x / y))

    def multiplication():
        print(float(x * y))

    if operation in 'asdm':
        if operation == 'a':
            addition()
        elif operation == 's':
            subtraction()
        elif operation == 'd':
            if y > 0:
                division()
            else:
                print("You can't divide by zero!")
        elif operation == 'm':
            multiplication()
    else:
        print('Error. This operation does not exist.')


calculate(7, 2, 'd')
