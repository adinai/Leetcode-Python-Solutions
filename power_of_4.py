#Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        ans = math.log(num, 4)
        if math.floor(ans) == math.ceil(ans):
            return True
        else:
            return False
