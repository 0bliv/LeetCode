class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            # Update current_sum to be either the current number alone, or add it to the existing subarray sum
            current_sum = max(num,current_sum + num)
            # Update the max_sum with the larger of current max_sum or the current_sum
            max_sum = max(max_sum,current_sum)       
        return max_sum
        