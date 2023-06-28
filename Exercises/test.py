# def factorial(a):
#     if(a>1):
#         a = a * factorial(a-1)
#     return a
#
# print(factorial(int(1)))

list = [8989, 113113, 12341234, 00, 44]
for num in list:
            index = 0
            for i in str(num):
                print(i, end='')
                index = index + 1
                if index == int(len(str(num))/2) :
                    break
            print()