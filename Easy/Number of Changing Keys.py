class Solution(object):
    def countKeyChanges(self, s):
        # Convert the string to lowercase once and store it
        s_lower = s.lower()
        
        # Initialize count of key changes
        key_changes = 0
        
        # Iterate through the string to count changes
        for i in range(1, len(s_lower)):
            if s_lower[i] != s_lower[i-1]:
                key_changes += 1
        
        return key_changes
