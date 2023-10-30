# Hangman Game

# Imports
import random


def play():
    start_game()

    secret_word = choose_secret_word()

    times = 5
    lose = False
    win = False

    correct_letters = start_correct_word(secret_word)

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


def start_game():
    print("******************************************")
    print("*   **   **   **   **   **   **   **   *")
    print("* HANGMAN * HANGMAN * HANGMAN * HANGMAN *")
    print("*   **   **   **   **   **   **   **   *")
    print("******************************************")


def choose_secret_word():
    #  Read the file of secret words
    file = open('secret_words.txt', 'r')
    words = []
    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    #  Select a ramdom word
    number = random.randrange(0, len(words))
    secret_word = words[number].lower()

    return secret_word


def start_correct_word(secret_word):
    return ['_' for letter in secret_word]


if __name__ == '__main__':
    play()

