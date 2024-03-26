import random

def get_questions():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Paris', 'Berlin', 'Madrid', 'Rome'],
            'correct_answer': 'Paris'
        },
        {
            'question': 'Which planet is closest to the Sun?',
            'options': ['Mercury', 'Venus', 'Earth', 'Mars'],
            'correct_answer': 'Mercury'
        },
        {
            'question': 'Which is the largest ocean?',
            'options': ['Pacific', 'Atlantic', 'Indian', 'Southern'],
            'correct_answer': 'Pacific'
        }
    ]
    return questions

def ask_question(question):
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f'{i + 1}. {option}')
    while True:
        try:
            user_answer = int(input('Enter the number of your answer: '))
            if 1 <= user_answer <= len(question['options']):
                return user_answer - 1
            else:
                print(f'Invalid input. Please enter a number between 1 and {len(question["options"])}.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def check_answer(user_answer, correct_answer_index, question):
    if user_answer == correct_answer_index:
        print('Correct!')
        return True
    else:
        print(f'Incorrect. The correct answer is {correct_answer_index + 1}. {question["options"][correct_answer_index]}.')
        return False

def main():
    questions = get_questions()
    random.shuffle(questions)
    score = 0
    for question in questions:
        user_answer_index = ask_question(question)
        if check_answer(user_answer_index, question['options'].index(question['correct_answer']), question):
            score += 1
    print(f'Your final score is {score}/{len(questions)}.')

if __name__ == '__main__':
    main()
