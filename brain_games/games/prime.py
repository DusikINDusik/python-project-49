import random

def is_prime():
    
    number = random.randint(1, 1000)
    
    if number < 2:
        return False
    elif number in (2, 3):
        correct_answer = 'yes'
    
    for prime_number in range(2, number - 1):
        if  number % prime_number == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    
    return str(number), correct_answer
           

    