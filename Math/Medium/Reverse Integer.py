class Solution(object):
    def reverse(self, x):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # Convert the integer to a string for easier manipulation
        str_x = str(x)

        # Handle negative numbers
        if str_x[0] == '-':
            reversed_x = int('-' + str_x[:0:-1])  # Reverse digits, excluding the '-'
        else:
            reversed_x = int(str_x[::-1])  # Reverse all digits

        # Check if reversed integer is within the 32-bit signed integer range
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
        else:
            return reversed_x
