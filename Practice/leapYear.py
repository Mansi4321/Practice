def is_leap(year):
    leap = False

    if (year % 400 == 0):
        leap = True
    else:
        if (year % 100 == 0):
            leap = False
        elif (year % 4 == 0):
            leap = True

    return leap


year = int(input('Enter a number: '))
print(is_leap(year))