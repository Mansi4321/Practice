"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a
single-digit number is produced. The input will be a non-negative integer.
"""

# #####1
def digital_root(n):
    if(n < 10):
        return n
    else:
        n=n%10+digital_root(n//10)
        return digital_root(n)


#####2
# def digital_root(n):
#     return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))

#####3
def digital_root1(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root1(root)
    return root


x = int(input("Please enter a number to find its digital root:\n"))
print(digital_root1(x))

# print(911//10)      #It gives 91 as answer.
# print(911/10)         #It gives 91.1 as answer
# print(911%10)       #It gives 1 as answer i.e. reminder of the equation