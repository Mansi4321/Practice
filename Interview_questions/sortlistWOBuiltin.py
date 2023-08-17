lis = [1, 12, 32, 53, 98, 56, 13]

##Descending order
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        if lis[i] < lis[j]:
            lis[i], lis[j] = lis[j], lis[i]

print(lis[-2])

#Ascending order
##Descending order
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        if lis[i] > lis[j]:
            lis[i], lis[j] = lis[j], lis[i]

print(lis[1])