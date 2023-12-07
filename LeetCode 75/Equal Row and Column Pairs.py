class Solution(object):
    def equalPairs(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # Check for each row if it matches any column
        for i in range(rows):
            for j in range(cols):
                if grid[i] == [grid[k][j] for k in range(rows)]:
                    count += 1

        return count
