class Solution(object):
    def reverseVowels(self, s):
        a = 0
        b = len(s) - 1
        vowels = "aeiouAEIOU"
        s = list(s)

        while a < b:
            while a < b and s[a] not in vowels:
                a+=1
            while a < b and s[b] not in vowels:
                b-=1
            
            if a < b:
                s[a], s[b] = s[b], s[a]
                a+=1
                b-=1

        return ''.join(s)

