# # Printing from left 1 to max stars
n = int(input("Please enter no of rows: "))

a = 1

while a <= n :      # This loop handles no of rows
    b = 1
    while b <= a :      # this loop handles no of stars
        print("*", end= " ")
        b += 1
    print()      #This print statement is used to print the stars from next loop in new line otherwise all stars will come in 1 line
    a += 1
#
# #Printing from left Max stars to 1
# n = int(input("Please enter no of rows: "))
#
# a = 1
#
# while a <= n :      # This loop handles no of rows
#     b = n
#     while b >= a :
#         print("*", end=" ")
#         b = b - 1
#     print()
#     a = a + 1

# Printing from Right 1 to max stars
# This is the example of print simple reversed right angle pyramid pattern
rows = int(input("Enter the number of rows:"))
k = 2 * rows - 2  # It is used for number of spaces
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2   # decrement k value after each iteration
    for j in range(0, i + 1):
        print("* ", end="")  # printing star
    print("")

