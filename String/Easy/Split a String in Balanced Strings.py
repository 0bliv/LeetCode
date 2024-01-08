class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_R = 0
        c_L = 0
        c_Max = 0

        for i in s:
            if i == 'L':
                c_L+=1
            elif i == 'R':
                c_R+=1
            if c_R == c_L:
                c_Max+=1
                c_R = 0
                c_L = 0
        return c_Max

        
        