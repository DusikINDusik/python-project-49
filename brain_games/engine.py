import prompt

def games_engine(get_question_and_answer, description):
    print ('Welcome, to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    correct_answer_count = 0

    while correct_answer_count < 3:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong ;(. Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            break
        
    if correct_answer_count == 3:
        print(f"Congratulations, {name}!")