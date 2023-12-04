class Solution(object):
    def compress(self, chars):
        if not chars:
            return 0

        index = 0  # Index to keep track of the current position in the modified chars array
        count = 1  # Counter to count consecutive characters

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[index] = chars[i - 1]  # Set the character at the current index
                index += 1

                if count > 1:  # If count is greater than 1, update chars array with count digits
                    for digit in str(count):
                        chars[index] = digit
                        index += 1

                count = 1  # Reset the count for the new character

        chars[index] = chars[-1]  # Set the character at the last index
        index += 1

        if count > 1:  # If count is greater than 1, update chars array with count digits
            for digit in str(count):
                chars[index] = digit
                index += 1

        return index  # Return the new length of the modified array
