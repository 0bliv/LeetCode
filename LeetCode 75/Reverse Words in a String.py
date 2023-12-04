class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        return ' '.join(w[::-1])
        