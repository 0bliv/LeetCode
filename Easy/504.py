class Solution(object):
    def convertToBase7(self, num):
        #Edge case for zero
        if num == 0:
            return "0"
    
        # Handle negative numbers
        is_negative = num < 0
        num = abs(num)
    
        # Convert to base 7
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7
    
         # If the number was negative, add the minus sign
        if is_negative:
         result.append('-')
    
        # Join the result list in reverse order since we collected digits from least significant to most
        return ''.join(result[::-1])
        