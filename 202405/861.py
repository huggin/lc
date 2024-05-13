class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 - grid[i][j]

        ans = 0
        for j in range(m):
            cnt = 0
            for i in range(n):
                if grid[i][j] == 0:
                    cnt += 1
            if cnt + cnt < n:
                cnt = n - cnt
            ans += (1 << m - 1 - j) * cnt
        return ans
