"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print
out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number
given by the user.
"""
#1
Nmblist1 = [1,2,3,4,5,6,7,8,9,10]

for x in Nmblist1:
    if x<5 :
        print(x)
#2
Nmblist2 = [1,2,3,4,5,6,7,8,9,10]
returnlist2 = []

for x in Nmblist2:
    if x<5 :
        returnlist2.append(x)

print(returnlist2)

#3
Nmblist3 = [1,2,3,4,5,6,7,8,9,10]
returnlist3 = []

print("Please find the list present:\t{}".format(Nmblist3))

num = int(input("Please enter a number and we will print numbers smaller than it from the list:\t"))

for x in Nmblist3:
    if x < num:
        returnlist3.append(x)

print(returnlist3)