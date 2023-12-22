class Solution(object):
    def countSetBits(self, n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    def sumIndicesWithKSetBits(self, nums, k):
        total_sum = 0
        
        for i, num in enumerate(nums):
            set_bits = self.countSetBits(i)
            if set_bits == k:
                total_sum += num
        
        return total_sum

