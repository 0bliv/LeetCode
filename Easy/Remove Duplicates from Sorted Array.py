class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        unique = set()
        index = 0
        
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
                nums[index] = nums[i]
                index+=1
        return len(unique)
