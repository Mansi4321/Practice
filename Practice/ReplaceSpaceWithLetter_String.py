"""
replace string space with a given character in Python

Example 1: a user has provided the string “l vey u” and the character “o”, and the output will be “loveyou”.

Example 2: a user has provided the string “D t C mpBl ckFrid yS le” and the character “a”, and the output will be
“DataCampBlackFridaySale”.
"""


def str_replace(text, ch):
    result = ''
    for i in text:
            if i == ' ':
                i = ch
            result += i
    return result


text = "D t C mpBl ckFrid yS le"
ch = "a"

print(str_replace(text,ch))