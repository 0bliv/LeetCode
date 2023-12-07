class Solution(object):
    def uniqueOccurrences(self, arr):
        c = {}

        for i in arr:
            c[i] = c.get(i,0)+1
        
        return len(c.values()) == len(set(c.values()))

        