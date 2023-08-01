#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = [int(x) for x in input("Please enter first 2 numbers of the series separated by comma:\t").split(",")]
print(a, end= " ")
while b < 1000:
    print(b, end = ' ')
    a, b = b, a + b

# print() # line ending

#Get n th number in fibonacci series
def fibonacci(n):
    a = int(input("Enter first number of the series"))
    b = int(input("Enter second number of the series"))
    if n<0:
        print("invalid input")
    elif n ==1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n+1):
            a, b = b, b+a
        return b

print(fibonacci(10))
