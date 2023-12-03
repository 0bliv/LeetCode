class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            if flowerbed[i] == 0:
                # Check if the current position is suitable for planting a flower
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # Plant a flower
                    count += 1  # Increment count for planted flowers
            i += 1
        
        return count >= n  # Check if count of planted flowers is greater than or equal to required 'n'
