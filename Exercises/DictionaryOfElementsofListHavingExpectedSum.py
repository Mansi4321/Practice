"""
l = [1,2,3,4,5,6,8]
sum = 9
output = {1:8,3:6,4:5}
"""

l = [1,2,3,4,5,6,8]
d = {}
s = 9

for i in range(len(l)):
    for j in range (1, len(l)):
        su = l[i] + l[j]
        if su == s:
            print(l[i], l[j])
            d.update({l[i]:l[j]})

print(d)