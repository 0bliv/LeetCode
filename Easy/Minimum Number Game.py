class Solution(object):
    def numberGame(self, nums):
        heapify(nums)
        resp = []

        while nums:
            a, b = heappop(nums), heappop(nums)
            resp.append(b)
            resp.append(a)
        return resp