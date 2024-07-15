class Solution(object):
    def singleNumber(self, nums):
        resp = 0
        for i in nums:
            resp ^= i
        return resp
        