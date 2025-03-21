# remove duplicate numbers from a given array. print number of unique values and print the array as only the unique
# values in their original array.

class Solution:
    def removeDuplicates(self, numsArray):
        # create a list to store unique values from input array
        seen = set()
        # counter for number of unique values
        k = 0
        
        # inspect each number in array; check if number is in seen array to track unique values; add if not already there
        for num in numsArray:
            if num not in seen:
                seen.add(num)
                numsArray[k] = num
                k += 1
        
        return k  

# Example
numsArray = [0, 0, 1, 1, 2, 3, 3]
obj = Solution()
k = obj.removeDuplicates(numsArray)

print("k:", k)  
print("Modified nums:", numsArray[:k])  


    

    
