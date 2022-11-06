import random

def check_number(user_input):
    if user_input < random_generated_number:
        return "Guessed number is low."
    elif user_input > random_generated_number:
        return "Guessed number is high."
    else:
        return "Guessed number is correct."

random_generated_number = random.randint(1,20)
# random_generated_number = 10
for chance in range(0,6):
    user_input = int(input("Guess the number: "))
    print(check_number(user_input))