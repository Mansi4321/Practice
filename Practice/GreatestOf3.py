### w/o using list

#1st way of taking inputs
# x = int(input("please enter first number: "))
# y = int(input("please enter second number: "))
# z = int(input("please enter third number: "))
# print(x,y,z)

#2nd way of taking inputs
# x, y, z = [int(x) for x in input("Enter the 3 numbers by pressing tab: ").split()]
# print(x,y,z)

#3rd way of taking inputs
x, y, z = [int(x) for x in input("Enter the 3 numbers by using comma: ").split(",")]
print(x,y,z)
# #
if x>y and x>z:
    print("{0} is greater than {1} and {2}".format(x,y,z))
elif y>z:
    # print("{1} is greater than {0} and {2}".format(x,y,z))
    print("%s is greater than %s and %s" %(y, x, z))
else :
    print("{2} is greater than {0} and {1}".format(x,y,z))

###Using list 1

#1st way of taking values
# a = list(map(int, input("please enter 3 numbers by pressing tab: ").split()))
# print(a)

#2nd way of taking values
# a = [int(x) for x in input("Enter 3 Numbers by pressing tab: "). split()]
# print(a)

#3rd way of taking values
# a = [int(x) for x in input("Enter 3 Numbers by using comma: "). split(",")]
# print(a)
# #
# if a[0]>a[1] and a[0]>a[2]:
#     print("{0} is greater than {1} and {2}".format(a[0],a[1],a[2]))
# elif a[1]>a[2]:
#     print("{1} is greater than {0} and {2}".format(a[0],a[1],a[2]))
# else :
#     # print("{2} is greater than {0} and {1}".format(a[0],a[1],a[2]))
#     print("%s is greater than %s and %s"%(a[2], a[0], a[1]))

