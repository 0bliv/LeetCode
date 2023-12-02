from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        # Initialize a defaultdict to store anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each word in the input list
        for word in strs:
            # Create a tuple of sorted characters to serve as the key
            sorted_word = ''.join(sorted(word))
            
            # Append the word to the corresponding group in the defaultdict
            anagrams[sorted_word].append(word)
        
        # Return the values of the defaultdict, which contain grouped anagrams
        return list(anagrams.values())
