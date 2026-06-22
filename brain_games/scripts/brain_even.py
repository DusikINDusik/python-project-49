import random
import prompt
from brain_games.cli import welcome_user

def is_even(number):
    return number % 2 == 0

def main():
    print('Welcome, to the Brain Games!')

    name = welcome_user()
    print(f"Hello, {name}!")

    print ('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answer_count = 0

    while correct_answer_count < 3:

        number = random.randint(1, 100)
        print (f'Question: {number}')

        if is_even(number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print('Correct!')
            correct_answer_count = correct_answer_count + 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}")
            break

    if correct_answer_count == 3:
        print(f"Congratulations, {name}")

if __name__ == '__main__':
    main()