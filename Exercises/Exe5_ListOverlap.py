"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""
from Resources.Functions import randomListCreation
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# commonlist= []
#
# for i in a:
#     if i in b:
#         if i not in commonlist:
#             commonlist.append(i)
#
# print(commonlist)

# print([x for x in a if x in b])  #Cannot get distinct results from this


### Using a function

randomlist1 = randomListCreation(10,0,4,1,10)
randomlist2 = randomListCreation(10,1,5,1,10)

randomlist1.sort()
randomlist2.sort()

print(randomlist1)
print(randomlist2)

outputlist = []
for x in randomlist1:
    if x in randomlist2 and x not in outputlist:
        outputlist.append(x)

print(outputlist)

