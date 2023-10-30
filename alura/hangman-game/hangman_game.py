# Hangman Game

def play():
    print("******************************************")
    print("*   **   **   **   **   **   **   **   *")
    print("* HANGMAN * HANGMAN * HANGMAN * HANGMAN *")
    print("*   **   **   **   **   **   **   **   *")
    print("******************************************")

    secret_word = 'banana'
    lose = False
    win = False
    times = 5
    correct_letters = ['_', '_', '_', '_', '_', '_']
    wrong_letters = []
    print(wrong_letters)

    while not lose and not win:
        guess = input('Type a letter: ').lower()
        guess = guess.strip()
        index = 0

        if guess in secret_word:
            for letter in secret_word:
                if letter == guess:
                    correct_letters[index] = letter
                    print(correct_letters)
                index += 1
        else:
            times -= 1

        if '_' not in correct_letters:
            print('You win! Congratulations!')
            win = True
        elif times < 1:
            print('You lose! Try again')
            print(f'The word was {secret_word}')
            lose = True


if __name__ == '__main__':
    play()
