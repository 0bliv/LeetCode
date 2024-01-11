class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle special cases
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == 0:
            return 0

        # Determine the sign of the quotient
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        result = sign * quotient

        # Check for overflow
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
