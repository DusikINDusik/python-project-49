import random

def is_progression(start, step, length_progression):
    
    progression = []

    for index in range(length_progression):
        currentElement = start + index * step
        progression.append(currentElement)
    return progression

def game_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 6)
    length_progression = random.randint(5, 10)

    random_element = random.randint(0, length_progression - 1)
    
    progression = is_progression(start, step, length_progression)

    correct_answer = progression[random_element]

    progression[random_element] = '..'

    progression = ' '.join([str(x) for x in progression])
    
    return progression, str(correct_answer)