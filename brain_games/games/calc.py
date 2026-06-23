import random

def calculate_game():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1 , 20)

    operation_sign = random.randint(1, 3)
    if operation_sign == 1:
        operation = '+'
    elif operation_sign == 2:
        operation = '-'
    else:
        operation = '*'

    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2

    expression = (f"{number_1} {operation} {number_2}")

    return expression, str(correct_answer)