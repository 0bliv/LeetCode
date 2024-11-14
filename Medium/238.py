class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1s.
    
        # Step 1: Calculate the left products for each element
        left_product = 1
        for i in range(n):
            result[i] = left_product  # Set result[i] to the product of all elements to the left of i
            left_product *= nums[i]  # Update left_product for the next iteration
    
        # Step 2: Calculate the right products for each element and multiply with left product
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product  # Multiply the current result with the product of all elements to the right of i
            right_product *= nums[i]  # Update right_product for the next iteration  