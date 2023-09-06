print("###############################")
print("###### The guessing game ######")
print("###############################")

secret_number = 23
total_tries = 3
tries = total_tries
rounds = 1

while rounds <= total_tries:
    print('Tries {} of {}'.format(rounds, total_tries))
    guess = int(input('Input a number: '))
    win = guess == secret_number

    greater = guess > secret_number
    lower = guess < secret_number

    if win:
        print('You win, the secret number is:', secret_number)
        break
    else:
        if greater:
            print('The number you guessed is less than the secret number!')
        elif lower:
            print('The number you guessed is greater than the secret number!')
        tries = tries - 1
        rounds = rounds + 1

print("Try again")
