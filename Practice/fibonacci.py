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
