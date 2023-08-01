"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import getpass
import sys

dict = ["rock", "paper", "scissors"]

print("\nWelcome to 2 player Rock, Paper and Scissors Game\n")

firstPlayer = input("Please enter 1st Player's Name:\n")
secondPlayer = input("\nPlease enter 2nd Player's Name:\n")


def playerChoice(arg):
    while True:
        choice = input("\n{}, Please select Rock, Paper or Scissors:\n".format(arg))        ##Comment this to play in windows command prompt
        # choice = stdiomask.getpass(prompt="\nPlease select Rock, Paper or Scissors:\n", mask='X')   ##Comment this to play in pycharm. In command prompt it shows X in place of words, so its predictable and useful for password entering. Not here
        # choice = getpass.getpass(prompt="\n{}, Please select Rock, Paper or Scissors:\n".format(arg))          ##Comment this to play in pycharm
        if choice.lower() in dict:
            return choice.lower()
        else:
            print("Invalid input! You have not entered rock, paper or scissors, try again.\n")
        # if choice.lower() not in dict:        ##it doesn't work as its creating an endless loop
        #     playerChoice(arg)

def compare(choice1, user1, choice2, user2):
    if choice1 == choice2:
        print("Its a tie")
    elif choice1 == "rock":
        if choice2 == "paper":
            print("{} wins!!!".format(user2))
        else:
            print("{} wins !!!".format(user1))
    elif choice1 == "paper":
        if choice2 == "scissors":
            print("{} wins!!!".format(user2))
        else:
            print("{} wins!!!".format(user1))
    elif choice1 == "scissors":
        if choice2 == "rock":
            print("{} wins!!!".format(user2))
        else:
            print("{} wins!!!".format(user1))


while True:
    x = input("\nDo you want to start a New Game? Yes or No?\n")

    if x.lower() == "yes":

        firstPlayerChoice = playerChoice(firstPlayer)
        secondPlayerChoice = playerChoice(secondPlayer)

        print("\n{} Selected {}\n".format(firstPlayer,firstPlayerChoice))
        print("{} Selected {}\n".format(secondPlayer,secondPlayerChoice))

        compare(firstPlayerChoice, firstPlayer, secondPlayerChoice, secondPlayer)


    elif x.lower() == "no":
        print("\nThank you for playing the game!!")
        # break
        sys.exit()

    else:
        print("\nInvalid input! You have not entered Yes or No, Please try again.")
        # break
        sys.exit()