# Secret word

secret_word = 'Anyone'.lower()
secret_word_len = len(secret_word)
wrong_word = secret_word.replace(secret_word, f'*' * secret_word_len)

correct_letters = ''

print(wrong_word)

tries = 0

while secret_word:
    letter = input('Type a letter: ').lower()
    tries += 1
    if len(letter) > 1:
        print('Type only a letter!')
        continue

    if letter in secret_word:
        correct_letters += letter
        print(correct_letters)

    word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            word += secret_letter
        else:
            word += '*'

    print(word)

    if word == secret_word:
        break

print(f'Nice you win! You try {tries}')