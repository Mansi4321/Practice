#### This is a recursive function. Recursive function calls itself
def factorial(num):
    if(num > 1):
        num = num * factorial(num-1)
    return num

x = int(input("Please enter a number to find its factorial:\t"))

print(factorial(int(x)))