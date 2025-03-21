# Given a zero-based permutation nums (0-indexed), build an array ans of the same length 
# where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Given:
class Solution:
    def buildArray(self, nums):
# MY CODE
        # given a random array, need to sort and put in numberical order.
        i = 0
        list = set()
        while True:
            try:
                for num in nums:
                    if nums[i] < nums[i + 1]:
                        list.add(num)
                return list
            except ValueError:
                
