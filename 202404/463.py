class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 1:
                ans += 1
            if grid[i][m - 1] == 1:
                ans += 1

        for j in range(m):
            if grid[0][j] == 1:
                ans += 1
            if grid[n - 1][j] == 1:
                ans += 1

        for i in range(n):
            for j in range(1, m):
                if grid[i][j] != grid[i][j - 1]:
                    ans += 1

        for j in range(m):
            for i in range(1, n):
                if grid[i - 1][j] != grid[i][j]:
                    ans += 1

        return ans
