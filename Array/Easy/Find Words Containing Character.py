class Solution(object):
    def findWordsContaining(self, words, x):
        resp = []
        c = 0
        for i in words:
            if x in i:
                resp.append(c)
            c+=1
        return resp