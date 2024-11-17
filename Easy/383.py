class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Create frequency counters
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)

        # Check if magazine has enough letters to form ransomNote
        for char,count in ransomNoteCount.items():
            if magazineCount[char] < count:
                return False
        return True