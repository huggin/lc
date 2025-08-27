class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dx = [1, 1, -1, -1]
        dy = [1, -1, -1, 1]
        n = len(grid)
        m = len(grid[0])

        @cache
        def go(r, c, d, t):
            nr = r + dx[d]
            nc = c + dy[d]
            ans = 1
            if 0 <= nr < n and 0 <= nc < m and (grid[r][c] != 1 and grid[nr][nc] + grid[r][c] == 2 or t == 0 and grid[r][c] == 1 and grid[nr][nc] == 2):
                ans = max(ans, 1 + go(nr, nc, d, t))
            if t == 0 and grid[r][c] != 1:
                d = (d + 1) % 4
                nr = r + dx[d]
                nc = c + dy[d]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] + grid[r][c] == 2:
                    ans = max(ans, 1 + go(nr, nc, d, 1))
            
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for k in range(4):
                        ans = max(ans, go(i, j, k, 0))
        return ans
