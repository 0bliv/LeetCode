class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)  # Sort the array to compare with the original
        count = {}  # Dictionary to store count of smaller numbers
        for index, num in enumerate(sorted_nums):
            if num not in count:  # Store the smallest index for each unique number
                count[num] = index
        result = []
        for num in nums:
            result.append(count[num])  # Retrieve counts from the dictionary
        return result