"""
Input : list1 = [1, 2, 3, 4, 5]
        list2 = [5, 6, 7, 8, 9]
Output : {5}
Explanation: The common elements of
both the lists are 3 and 4

Input : list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9]
Output : No common elements
Explanation: They do not have any
elements in common in between them
"""
"""
1:Convert the lists to sets and then print set1&set2. set1&set2 returns the common elements set, 
where set1 is the list1 and set2 is the list2. 
"""

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)

"""
Method 2:Using Set’s intersection property
"""


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return (a_set.intersection(b_set))
    else:
        return ("no common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))