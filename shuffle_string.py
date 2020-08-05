# 1528. Shuffle String Leetcode

""" 
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans =""
        l = len(s)
        for i in range(l):
            for j in range(l):
                if i == int(indices[j]):
                    ans += s[j]
        return ans
                    
