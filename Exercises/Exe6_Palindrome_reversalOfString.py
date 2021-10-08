"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads
 the same forwards and backwards.)"""

########---------1
#We need to use lower function at least once for palindrome

wrd = str(input("Please enter a string to check if palindrome:\t"))

wrd_filtered = ''.join(i.lower() for i in wrd if i.isalnum())      ##filtering string into alphanumeric is very important for palindrome

rvs=wrd_filtered[::-1]

# print(rvs)

if wrd_filtered == rvs:      ##wrd.lower() == rvs.lower()
    print("The word is palindrome")
else:
    print("The word is not palindrome")

########---------2

def reverse(word):
	x = ''
	for i in range(len(word)):
                # x += word[len(word) - i -1] is same as  x=x+word[len(word)-i-1]
                x = x + word[len(word) - i - 1]

                """For ex: suppose, the word is Amit.
                so its length is 4.

                for i in range(4):
                    x = x + word [4 - i - 1]  ##in the square brackets "[]", we are trying to get the index of 't' from word Amit
                                                            A,m,i,t
                 as range is given as 4, i can have values: 0,1,2,3

                 for i = 0, x is empty i.e. x = ''
                 x = x + word [4 - 0 - 1]   i.e. x = x + word[3]   so in word letter present at 3rd index is t. so,
                 x = '' + 't'
                 x = 't'
                 return x: it returns value of x as t

                 for next loop where i = 1
                 x = x + word[4-i-1]
                 x = 't' + word[4-1-1]
                 x = 't' + word[2]
                 x = 't' + 'i'
                 x = 'ti'

                 In similar way we finally get the reverse of the string.
                """
	return x

word = input('give me a word:\n')
word_fltr = ''.join(c.lower() for c in word if c.isalnum())
# print(len(word))
x = reverse(word_fltr)
# print(x)
if  x == word_fltr  :                  ##x.casefold() == word_fltr.casefold():
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')

########---------3

def is_palindrome(input_str):
    filtered_str = "".join(c.lower() for c in input_str if c.isalnum())
    """The above line of code is very important for palindrome as filters the entered string into
    lowercase alphanumeric string which ignores symbols, so we get a string to compare
    for ex: Don't nod.  this is a palindrome. but if we don't use above function, it will not return as palindrome
    after using above code the string is converted to: dontnod
    """
    return filtered_str == filtered_str[::-1]
    # filtered_str[::-1] reverses the string. and this line of code returns a boolean ie True False if the strings match

inputstr = str(input("please enter a string to check if palindrome:\n"))

x = is_palindrome(inputstr)

if x == True:   ### Need to enter this value as True only and not as true.
    print("This is palindrome")
else:
    print("not a palindrome")