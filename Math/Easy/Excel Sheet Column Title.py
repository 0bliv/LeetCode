class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        column_title = ""
        
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26  # Get the remainder
            columnNumber = (columnNumber - 1) // 26  # Update columnNumber
            
            # Convert the remainder to corresponding character and append to the title
            column_title = chr(65 + remainder) + column_title

        return column_title
