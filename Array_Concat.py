# Given an integer array nums of length n, you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Given:
class Solution:
    def getConcatenation(self, nums):
# my code
        # need to take one given array and insert same aray into itself 
        ans = nums + nums    
        return ans

object = Solution()
result = object.getConcatenation([1, 2, 1])
print(result)