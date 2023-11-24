class Solution(object):
    def arraySign(self, nums):
        total = 1
        
        if 0 in nums:
            return 0
        
        for i in nums:
            total *= i
        
        if total > 0:
            return 1
        else:
            return -1

        