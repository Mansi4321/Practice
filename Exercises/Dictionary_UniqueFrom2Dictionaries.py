"""
d1 = {a:30,b:40,c:50,d:300}
d2 = {b:40,c:70,d:300}

op = {b:40,d:300}
"""
d1 = {'a':30,'b':40,'c':50,'d':300}
d2 = {'b':40,'c':70,'d':300}
d3 = {}

for i in d1:
    if i in d2:
        value1 = d1.get(i)
        value2 = d2.get(i)
        if value1 == value2:
            d3.update({i:value1})

print(d3)
