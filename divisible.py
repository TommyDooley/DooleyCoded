def divisible(x):
    if x % 3 == 0 and x % 5 == 0:
        return "BINGO!"
    elif x % 5 == 0:
        return "Divisible by 5, but not 3"
    elif x % 3 == 0:
        return "Divisible by 3, but not 5"
    else:
        return "Not Quite"

print(divisible(int(input('Pick a number divisible by 3 and 5: '))))