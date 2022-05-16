import random

def computer_guess(x,y):
    low = x
    high = y
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (h), too low (l), or just right (c)?")
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Great work! {guess}")

computer_guess(10,20)
