class Solution(object):
    def minOperations(self, nums, k):
        c = 0
        for i in nums:
            if i < k:
                c+=1
        return c
        