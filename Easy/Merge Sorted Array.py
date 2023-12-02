class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        p = m + n - 1  # Pointer for merged nums1

        # Merge nums1 and nums2 from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 has remaining elements, add them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
