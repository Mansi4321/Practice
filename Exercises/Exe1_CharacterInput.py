"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them
the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
 (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the
ENTER button)
"""

# importing date class from datetime module
from datetime import date

# creating the date object of today's date
# todays_date = date.today()

# printing todays date
# print("Current date: ", todays_date)

#Fetching current year
CurrentYear= date.today().year

name, age = input("Please enter your Name and Age separated by tab: ").split()
birthYear = CurrentYear - int(age)
OutputYear = birthYear + 100

print("Hi %s, You will turn 100 year old in %s"%(name,OutputYear))
print(name + " will be 100 years old in the year " + str(OutputYear))

expectedLines = int(input("Please enter a Number: "))

for x in range(expectedLines):
    print("Hi {}, You will turn 100 year old in {}\n".format(name, OutputYear))

