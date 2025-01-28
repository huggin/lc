class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        v = [[0] * n for _ in range(m)]

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        def dfs(i, j):
            ans = grid[i][j]
            v[i][j] = 1
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] > 0 and v[ni][nj] == 0:
                    ans += dfs(ni, nj)
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if v[i][j] == 0 and grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        return ans
