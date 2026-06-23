import random

def is_even():
    number = random.randint(1, 100)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer

