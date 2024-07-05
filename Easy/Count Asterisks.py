class Solution(object):
    def countAsterisks(self, s):
        resp = 0
        x = False
        
        for i in s:
            if i == '|':
                x = not x
            elif i == '*' and not x:
                resp+=1
        return resp
