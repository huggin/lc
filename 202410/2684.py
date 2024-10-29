class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 0

        ans = 0
        for i in range(1, n):
            for j in range(m):
                if j - 1 >= 0 and dp[j-1][i-1] >= 0 and grid[j-1][i-1] < grid[j][i]:
                    dp[j][i] = i
                elif j + 1 < m and dp[j+1][i-1] >= 0 and grid[j+1][i-1] < grid[j][i]:
                    dp[j][i] = i
                elif dp[j][i-1] >= 0 and grid[j][i-1] < grid[j][i]:
                    dp[j][i] = i
        
                ans = max(ans, dp[j][i])
        
        return ans

