#Given a string, find the first non-repeating character and return its index. If all characters repeat, return -1.

#import applicable modules
from collections import Counter

Uinput = input("Enter a single word. ")

def character_indexer(Uinput):
#need to take string and and count how often characters appear
    #how does python count characters
    char_count = Counter(Uinput)
#find the first one that only occurs once
    #how does pythong check the order?
    for index, char in enumerate(Uinput):
        if char_count[char] == 1:
            return index
    
#return -1 if no unique characters
    return -1

print(character_indexer(Uinput))