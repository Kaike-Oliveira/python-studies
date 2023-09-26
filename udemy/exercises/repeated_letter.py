# Most repeated letter

phrase = 'Python is a programming language, created by Guido van Rossum'

i = 0
qtd_appears = 0
letter_most_appears = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1
        continue

    letters_time = phrase.count(current_letter)

    if qtd_appears < letters_time:
        qtd_appears = letters_time
        letter_most_appears = current_letter

    print(current_letter, letters_time)
    i += 1

print(f'The letter most appears was {letter_most_appears}, it appears {qtd_appears}x')
