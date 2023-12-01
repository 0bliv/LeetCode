class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1  # Move backward pointer to the left
            else:
                left += 1  # Move forward pointer to the right
        
        return left
