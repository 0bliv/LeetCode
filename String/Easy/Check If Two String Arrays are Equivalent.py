class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
         # Concatenate elements in word1 array to form a string
        string1 = ''.join(word1)
    
        # Concatenate elements in word2 array to form a string
        string2 = ''.join(word2)
    
        # Compare the two strings and return True if they are equal, otherwise return False
        return string1 == string2
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        