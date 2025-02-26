# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
from itertools import count

#Leetcode 58
s ="Hello World"

def lengthword(s:str):
    newstr = s.strip(" ").split(" ")
    return len(newstr[-1])


print(lengthword(s))