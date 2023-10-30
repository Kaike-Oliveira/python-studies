# Hangman Game

def play():
    print("******************************************")
    print("*   **   **   **   **   **   **   **   *")
    print("* HANGMAN * HANGMAN * HANGMAN * HANGMAN *")
    print("*   **   **   **   **   **   **   **   *")
    print("******************************************")

    secret_word = 'universe'
    lose = False
    win = False
    times = 5
    word = ''
    wrong_letters = []

    while not lose and not win:
        guess = input('Type a letter: ').lower()
        index = 0

        for letter in secret_word:
            if letter == guess:
                print(f'Correctly letter {letter} in position {index}!')
                print()
            index += 1

        if word == secret_word:
            print('You win! Congratulations!')
            win = True
        elif times < 1:
            print('You lose! Try again')
            print(f'The word was {secret_word}')
            lose = True


if __name__ == '__main__':
    play()
