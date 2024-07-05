class Solution(object):
    def isPalindrome(self, s):
        # Preprocess the string: convert to lowercase and remove non-alphanumeric characters
        processed_s = ''.join(char.lower() for char in s if char.isalnum())

        # Check if the processed string is equal to its reversed form
        return processed_s == processed_s[::-1]
