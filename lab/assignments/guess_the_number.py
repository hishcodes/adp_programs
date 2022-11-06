import random
import sys

def guess_number(user_input):
    if user_input == generated_number:
        return 'You won guessed it correct. You won!'
    elif user_input < generated_number:
        return 'guessed number is too low'
    else:
        return 'guessed number is too high'

generated_number = random.randint(1,20)

for chance in range(1,7):
    user_input = int(input("Guess the number: "))
    print(guess_number(user_input))
    if user_input == generated_number:
        sys.exit()