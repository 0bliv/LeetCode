from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Check if the sets of characters are the same in both strings
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if the frequencies of characters are the same
        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())

        return freq1 == freq2
