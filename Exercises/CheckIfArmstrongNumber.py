"""
For eg: 153, is an Armstrong number because it has 3 digits, and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""

a = 1634

exponent = len(str(a))
list1 = []
for i in str(a):
    b = int(i) ** exponent
    list1.append(b)

sum = 0
for j in list1:
    sum = sum + j

if sum == a:
    print("Armstrong Number")
else:
    print("not armstrong")