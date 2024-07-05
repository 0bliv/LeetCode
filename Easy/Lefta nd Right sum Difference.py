class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        r_sum = sum(nums)
        l_sum = 0
        resp = [0]*n
        
        for i in range(n):
            l_sum += nums[i]
            resp[i] = abs(l_sum - r_sum)
            r_sum-=nums[i]

        return resp