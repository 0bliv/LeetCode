class Solution(object):
    def subtractProductAndSum(self, n):
        sum_digits = 0
        product_digits = 1

        for i in str(n):
            sum_digits += int(i)
            product_digits *= int(i)       
        return product_digits - sum_digits
