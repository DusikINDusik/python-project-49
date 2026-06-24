import random

def is_gcd(number_1, number_2):
    while number_2 != 0:
        temp_number = number_1 % number_2
        number_1 = number_2
        number_2 = temp_number
    return number_1

def is_game_gcd():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    question = (f'{number_1} {number_2}')

    correct_answer = is_gcd(number_1, number_2)

    return question, str(correct_answer)