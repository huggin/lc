class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        d = [(-1, 0),(0, -1), (0, 1), (1, 0)]
        
        def dfs(grid, i, j, visited): 
            for k in range(4):
                ni = i + d[k][0]
                nj = j + d[k][1]
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and grid[i][j] == 1:
                    visited[ni][nj] = 1
                    dfs(grid, ni, nj, visited)
        def go(grid):
            visited = [[0 for _ in range(m)] for _ in range(n)]
            cnt = 0
            for i in range(n):
                for j in range(m):
                    if visited[i][j] == 0 and grid[i][j] == 1:
                        cnt += 1 
                        dfs(grid, i, j, visited)
            return cnt
        
        cnt = go(grid)
        if cnt >= 2 or cnt == 0:
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cnt = go(grid)
                    if cnt >= 2 or cnt == 0:
                        return 1
                    grid[i][j] = 1
        
        return 2
