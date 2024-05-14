class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        n = len(grid)
        m = len(grid[0])
        v = [[0 for _ in range(m)] for _ in range(n)]

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        def f(i, j, curr):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if (
                    ni >= n
                    or ni < 0
                    or nj >= m
                    or nj < 0
                    or v[ni][nj] == 1
                    or grid[ni][nj] == 0
                ):
                    continue
                v[ni][nj] = 1
                f(ni, nj, curr + grid[ni][nj])
                v[ni][nj] = 0
            self.ans = max(self.ans, curr)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    v[i][j] = 1
                    f(i, j, grid[i][j])
                    v[i][j] = 0

        return self.ans
