import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low < high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be hi b/c low = high

        feedback = input(f"Is {guess} too high(H) or too low(L) or correct(C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess} correctly")

high = 1000
print(f"Think of a number between 1 and {high}. The computer will guess it for you")
computer_guess(high)
