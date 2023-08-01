a = {1, 2, 3, 5, 'ABC'}

b = set((1, 2, 4, 'bc'))

c = a.union(b)
print(c)

c = a.update(b)
d = a.intersection(b)
e = a.difference(b)

print(c)
print(d)
print(e)

a.update((7,))
a.remove(7)
a.discard(3)
a.pop()

print(a)

a.clear()
print(a)