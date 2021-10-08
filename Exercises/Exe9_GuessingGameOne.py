"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random
import sys


def guess_check():
    if guess == num:
        print("Exactly Correct")
        print("You took only {} tries".format(c))
    elif guess > num:
        print("Guessed too high".format(num))
    else:
        print("Guessed too low".format(num))

num = random.randint(1,9)
print(num)
guess = 0
c = 0

while guess != num and guess != "exit":
    print(guess, c)
    guess = (input("\nPlease guess the number from 1 to 9 or enter \"exit\" to exit the game:\n"))

    if guess.lower() == "exit":
        sys.exit()
    guess = int(guess)
    c = c + 1
    guess_check()