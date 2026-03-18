class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    ans += 1
                else:
                    break
        return ans

