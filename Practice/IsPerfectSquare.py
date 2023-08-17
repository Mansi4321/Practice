import math

num = 37
squareRoot = math.isqrt(num)

square = squareRoot * squareRoot

if num == square:
    print("Given number " +str(num) + " is a perfect square")
else:
    print("Given number " +str(num) + " is not a perfect square")
