from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        # Create a Counter of elements in nums
        counter = Counter(nums)
        
        # Use Counter's most_common method to get the k most common elements
        most_common_elements = counter.most_common(k)
        
        # Extract the elements from the Counter object
        result = [element[0] for element in most_common_elements]
        
        return result
