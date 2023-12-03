class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        comp = max(candies)
        return [c + extraCandies >= comp for c in candies]

        