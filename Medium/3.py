class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = set()
        max_length = 0

        for rigth in range(len(s)):
            while s[rigth] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[rigth])
            max_length = max(max_length, rigth - left +1)
        
        return max_length