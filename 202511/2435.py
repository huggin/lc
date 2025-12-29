class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    for kk in range(k):
                        dp[i][j][(kk + grid[i][j]) % k] += dp[i - 1][j][kk]
                if j - 1 >= 0:
                    for kk in range(k):
                        dp[i][j][(kk + grid[i][j]) % k] += dp[i][j - 1][kk]
        return dp[m - 1][n - 1][0] % MOD
