from collections import Counter
class Solution(object):
    def findTheDifference(self,s,t):
        s_count = Counter(s)
        t_count = Counter(t)
        for char, count in t_count.items():
            if count > s_count[char]:
                return char
        return ""
