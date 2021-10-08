# Decide the numbers of inputs.
n = int(input("Please enter total No of input values:\n"))

lst = []
for i in range(n):
    lst.append(int(input()))

print(lst)

def Sum(num):
    a = 0
    for i in num:
        a = a + i
    return a

print(sum(lst))