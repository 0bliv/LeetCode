class Solution(object):
    def numIdenticalPairs(self, nums):
        num_count = {}
        good_pairs = 0
        
        # Count occurrences of each number in the array
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Calculate the number of good pairs for each number that occurs more than once
        for count in num_count.values():
            if count > 1:
                # For n occurrences of a number, n choose 2 gives the count of good pairs
                good_pairs += (count * (count - 1)) // 2
        
        return good_pairs
