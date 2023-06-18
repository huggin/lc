class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        M = int(1e9 + 7)

        dp = [[-1 for _ in range(m)] for _ in range(n)]
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = 1
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (ni >= 0 and ni < n and nj >= 0 and nj < m):
                    continue
                if grid[i][j] < grid[ni][nj]:
                    if dp[ni][nj] == -1:
                        dfs(ni, nj)

                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % M
            return dp[i][j]

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = (ans + dfs(i, j)) % M

        return ans
