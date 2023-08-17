def power(base, exponent):
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    elif exponent > 1:
        base = base * power(base, exponent-1)
        return base
    elif exponent < 0:
        newExponent = abs(exponent)     #absolute value is a python in built method. absolute value of -6 will be 6
        # print(newExponent)
        base= base * power(base, newExponent-1)
        # print(base)
        return 1/base

# a = int(input("Please enter base number:\t"))
# b = int(input("Please enter Exponent value:\t"))


a , b = [int(x) for x in input("Please enter base and exponent separated by comma:\t").split(",")]

x = power(a, b)

print(x)