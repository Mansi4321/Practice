"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
## the below example returns only unique values. So this is not the solution
def unique(iterable):
    unique = []
    for i in iterable:
        if i not in unique:
            unique.append(i)
    return unique

print(unique("AAAABBBCCDAABBB"))
#1
def unique_in_order(iterable):
    unique = []
    for i in iterable:
        if len(unique)<1 or not unique[len(unique) - 1] == i:
            unique.append(i)
    return unique
#2
def unique_in_order1(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order1([1,2,2,3,3,3,4,4,4,4]))

#3
def unique_in_order2(a):
    lst = []
    for i in a:
        if len(lst) == 0:
            lst.append(i)
        elif i != lst[-1]:
            lst.append(i)
    return lst

print(unique_in_order2("AAAABBBCCDAABBB"))