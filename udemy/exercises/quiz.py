# Quiz

questions = [
    {
        'Question': 'What the result of 2 + 2?',
        'Options': ['1', '2', '3', '4'],
        'Answer': '4',
    },
    {
        'Question': 'What the result of 5 * 5?',
        'Options': ['12', '25', '45', '30'],
        'Answer': '25',
    },
    {
        'Question': 'What the result of 10 / 2?',
        'Options': ['5', '2', '32', '14'],
        'Answer': '5',
    },
]

total = 0
questions_len = len(questions)

for question in questions:
    print(question['Question'])
    for option in question['Options']:
        print(option)

    # Gets the user answer
    answer = input('What the correctly? ')

    # Check if the answer is correct
    if answer == question['Answer']:
        print('Correctly! ✅')
        total += 1
    else:
        print('Wrong! ❌')

print(f'You got it right {total} of {questions_len} questions!')
