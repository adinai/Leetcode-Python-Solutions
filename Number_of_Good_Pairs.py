# Number of Good Pairs Python solution
"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if (nums[i] == nums[j]) and i < j:
                    count +=1
        return count
        
