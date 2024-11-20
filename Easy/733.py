class Solution(object):
    def floodFill(self, image, sr, sc, color):
        # The original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the color to flood is the same as the original color, no need to fill
        if original_color == color:
            return image

        # Helper function for DFS
        def dfs(r, c):
            # If the current pixel is out of bounds or not the original color, stop
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return
            
            # Change the color of the current pixel
            image[r][c] = color
            
            # Recursively flood fill the four adjacent pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        # Start the DFS from the given pixel
        dfs(sr, sc)
        
        return image