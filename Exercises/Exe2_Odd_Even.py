"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into
num, tell that to the user. If not, print a different appropriate message.

"""
x = int(input("Please enter a Number to check if odd or even: "))
if (x%2 == 0) and (x%4 == 0):
    print("%s is an even number and a multiple of 4" % (x))
elif (x%2 == 0):
    print("{} is an even number".format(x))
else:
    print("{} is an odd number".format(x))

num, check = [int(x) for x in input("Please enter 2 numbers in order to check if 1st divides evenly into 2nd:\t").split()]
if num%check == 0 :
    print("{} is completely divisible by {}".format(num, check))
else:
    print("%s is not completely divisible by %s"%(num,check))