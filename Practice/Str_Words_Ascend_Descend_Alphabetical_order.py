# Program to sort alphabetically the words form a string provided by the user
#Approach 1
string_To_Sort = input("Please enter a string to sort in alphabetical order:\t")

words = string_To_Sort.split()

print(words)

words.sort()

print(words)

words.sort(reverse=True)

print(words)

# ascend_str = Ascending_sort(words)
#
# print(ascend_str)

# for i in words:
#     print(i)
#
# # Approach 2
# my_str = input("Enter a string: ")
#
# # breakdown the string into a list of words
# words = [word.lower() for word in my_str.split()]
#
# # sort the list
# words.sort()
#
# # display the sorted words
#
# print("The sorted words are:")
# for word in words:
#    print(word)