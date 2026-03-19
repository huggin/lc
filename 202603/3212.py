class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp2 = [[False for _ in range(m)] for _ in range(n)]
        if grid[0][0] == 'X':
            dp[0][0] = 1
            dp2[0][0] = True
        elif grid[0][0] == 'Y':
            dp[0][0] = -1
            dp2[0][0] = True
        
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp2[i][0] = dp2[i-1][0]
            if grid[i][0] == 'X':
                dp[i][0] += 1
                dp2[i][0] = True
            elif grid[i][0] == 'Y':
                dp[i][0] -= 1
                dp2[i][0] = True

        for i in range(1, m):
            dp[0][i] = dp[0][i-1]
            dp2[0][i] = dp2[0][i-1]
            if grid[0][i] == 'X':
                dp[0][i] += 1
                dp2[0][i] = True
            elif grid[0][i] == 'Y':
                dp[0][i] -= 1
                dp2[0][i] = True
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
                dp2[i][j] = dp2[i-1][j] or dp2[i][j-1] 
                if grid[i][j] == 'X':
                    dp[i][j] += 1
                    dp2[i][j] = True
                elif grid[i][j] == 'Y':
                    dp[i][j] -= 1
                    dp2[i][j] = True
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0 and dp2[i][j]:
                    ans += 1
        return ans

