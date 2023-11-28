class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""    

        strs.sort()
        p = strs[0]
        u = strs[-1]
        i = 0

        while i < len(p) and i < len(u) and p[i] == u[i]:
            i+=1
        return p[:i]

        