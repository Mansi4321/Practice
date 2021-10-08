import random
####1
a = list(random.sample(range(30), 10 + random.randrange(4)))
b = list(random.sample(range(40), 10 + random.randrange(6)))
a.sort()
b.sort()
print(a)
print(b)
print(list(set(a).intersection(set(b))))

####2
# a = [1, 2, 2]
# b = [1 , 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]
# c = (a + b)
# # print(c)
# new = []
#
# for i in c:
#     if i not in new:
#         new.append(i)
#
# print(new)

