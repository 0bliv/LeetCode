class Solution(object):
    def truncateSentence(self, s, k):
        x = s.split()
        resp = ' '.join(x[:k])
        return resp