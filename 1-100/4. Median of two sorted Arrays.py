class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two sorted arrays
        merged = []
        i, j = 0, 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
    
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
    
        # Calculate the median
        total_length = len(merged)
        middle = total_length // 2
    
        if total_length % 2 == 1:
            return merged[middle]
        else:
            return (merged[middle - 1] + merged[middle]) / 2.0
