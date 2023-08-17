list1 = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75]
#Approach 1
list2 = list1[::-1]

print(list2)

#Approach 2
list3 = []
for i in range(len(list1) - 1, -1, -1):
    list3.append(list1[i])

print(list3)
