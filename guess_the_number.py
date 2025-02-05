import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
thanks = 'Thanks, '


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """

    guess = input('Please guess the number: ')
    while guess.isnumeric() is False:
        guess = input('Guess must be a number: ')

    return int(guess)   



def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    total_guess = 0


    while True:
        guess = get_guess()
        total_guess = total_guess + 1
        result = check_guess(guess, secret)
        print(thanks,result)

        if result == correct:
            break

    print('Thanks for playing the game!')
    print(f'It took you {total_guess} guesses to figure it out!')

if __name__ == '__main__':
    main()
