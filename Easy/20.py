class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # if char is an opening bracket
                stack.append(char)
            elif char in mapping:  # if char is a closing bracket
                if not stack:
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
        
        return len(stack) == 0
