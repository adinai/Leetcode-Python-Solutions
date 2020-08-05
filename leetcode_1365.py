# 1365. How Many Numbers Are Smaller Than the Current Number

"""

Given the array nums, for each nums[i] 
find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newlist = list()
        l = len(nums)
        for i in range(l):
            count = 0
            for j in range(l):
                if nums[i] > nums[j]:
                    count += 1
            newlist.append(count)
        return newlist
