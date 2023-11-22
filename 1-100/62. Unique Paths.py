class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use a 1D array to store intermediate results
        dp = [1] * min(m, n)

        for i in range(1, max(m, n)):
            for j in range(1, min(m, n)):
                dp[j] += dp[j - 1]

        return dp[-1]
