class Solution(object):
    def isPalindrome(self, s):
         # Clean up the string: lowercasing, removing non-alphanumeric characters
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        # Check if equals to reverse
        return cleaned == cleaned[::-1]