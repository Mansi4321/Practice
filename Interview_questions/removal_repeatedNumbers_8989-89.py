# 1 To remove from single number
num = 8989
# index = 0
# for i in str(num):
#     print(i, end='')
#     index = index + 1
#     if index == int(len(str(num))/2) :
#         break
# print()

# 2 To remove from a list of numbers
list = [8989, 113113, 12341234, 00, 44]
# for num1 in list:
#     index = 0
#     for i in str(num1):
#         print(i, end='')
#         index = index + 1
#         if index == int(len(str(num1)) / 2):
#             break
#     print()

# 3 to use the same for single number with a method in class or a simple method
# def test_remove(num):
#     list1=[]
#     index=0
#     for i in str(num):
#         list1.append(i)
#         index = index + 1
#         if index == int(len(str(num))/2):
#             break
#     return "".join(list1)
#
# print(test_remove(num))

def test_remove_from_list(list_test):
    list2 = []
    for num in list_test:
        list1=[]
        index=0
        for i in str(num):
            list1.append(i)
            index = index + 1
            if index == int(len(str(num))/2):
                break
        c = ''.join(list1)
        list2.append(c)

    return list2

print(test_remove_from_list(list))