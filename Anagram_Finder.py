#Given two strings, determine if one is an anagram of the other. 
#An anagram is when one word can be rearranged to form another by using all the same letters the same number of times.

#import applicable module
from collections import Counter

#create anagram finder function
def Anagram_Finder(input1, input2):
    #analyze our 2 input strings; they should look the same if they are anagrams so our check can return "not an Anagram quickly"
    c1 = Counter(input1)
    c2 = Counter(input2)
    #check the input verse one another; if the count is the same they are anagrams
    if c1 == c2:
        return f'"{input1}" and "{input2}" are anagrams!'
    else:
        #otherwise return "input is not an Anagram"
        return f'"{input1}" and "{input2}" are not anagrams'

print(Anagram_Finder("silent", "listen"))
print(Anagram_Finder("dog", "cat"))
print(Anagram_Finder("racecar", "carrace"))
