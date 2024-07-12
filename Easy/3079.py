class Solution(object):
    def sumOfEncryptedInt(self, nums):
        resp = 0
        for i in nums:
            if i >= 10:
                max_digit = max(str(i)) # find the biggest digit
                encrypted_digit = int(max_digit * len(str(i))) # Encrypted number as intenger
                resp+=encrypted_digit
            else:
                resp+=i
        return resp

        