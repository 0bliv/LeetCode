class Solution(object):
    def shuffle(self, nums, n):
        shuffled = [None] * (2 * n)
        for i in range(n):
            shuffled[2 * i] = nums[i]
            shuffled[2 * i + 1] = nums[n + i]
        return shuffled
        