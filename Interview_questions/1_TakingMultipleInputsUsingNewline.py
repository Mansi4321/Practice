# Decide the numbers of inputs.
n = int(input("Please enter total No of input values:\n"))

lst = []
for i in range(n):
    lst.append(int(input()))

lst1 = []
i = 0
while i < n:
    lst1.append(int(input("Please enter number {}:\t".format(i+1))))
    i = i + 1

print(lst)
print(lst1)

def Sum(num):
    a = 0
    for i in num:
        a = a + i
    return a

print(sum(lst))