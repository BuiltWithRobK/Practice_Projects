#Given a list of numbers and a target value, return the indices of the two numbers that add up to the target

#import modules to use
from collections import Counter
#create function def with a list and a single target parameter
def Number_Target(list, target):
    #for loop for length of list to test all values
    for i in range(len(list)):
        #for loop to make sure the next value in the list is checked without checking against itslef
        for j in range(i+1, len(list)):
            # if statement to check first indice and second indice equalling target
            if list[i]+list[j] == target:
                #if any check is true, return the two indices
                return [i,j]

    #if none add to target return  
    return f'no values add up to "{target}"' 

print(Number_Target([1, 2, 3, 4], 6))