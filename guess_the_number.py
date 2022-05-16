import random

def guess(y,x):
    random_number = random.randint(y,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between {y} and {x}: "))
        if guess < random_number:
            print('Too low!')
        elif guess > random_number:
            print("Too high!")
        
    print(f"Good job! {guess}")

guess(5,10)