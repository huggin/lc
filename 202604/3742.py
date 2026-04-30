class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-2000] * (k + 1) for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    for kk in range(k + 1):
                        if grid[i][j] == 0:
                            dp[i][j][kk] = 0
                        elif kk < k:
                            dp[i][j][kk + 1] = gird[i][j]
                elif i == 0:
                    for kk in range(k + 1):
                        if grid[i][j] == 0:
                            dp[i][j][kk] = dp[i][j - 1][kk]
                        elif kk >= 1:
                            dp[i][j][kk] = dp[i][j - 1][kk - 1] + grid[i][j]
                elif j == 0:
                    for kk in range(k + 1):
                        if grid[i][j] == 0:
                            dp[i][j][kk] = dp[i - 1][j][kk]
                        elif kk >= 1:
                            dp[i][j][kk] = dp[i - 1][j][kk - 1] + grid[i][j]
                else:
                    for kk in range(k + 1):
                        if grid[i][j] == 0:
                            dp[i][j][kk] = max(dp[i - 1][j][kk], dp[i][j - 1][kk])
                        elif kk >= 1:
                            dp[i][j][kk] = (
                                max(dp[i - 1][j][kk - 1], dp[i][j - 1][kk - 1])
                                + grid[i][j]
                            )

        ans = max(dp[m - 1][n - 1])
        return ans if ans >= 0 else -1
