class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, pi=-1, pj=-1):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] == grid[ni][nj]:
                    if ni == pi and nj == pj:
                        continue
                    if visited[ni][nj] == 1:
                        return True
                    elif visited[ni][nj] == 2:
                        continue
                    else:
                        visited[ni][nj] = 1
                        if dfs(ni, nj, i, j):
                            return True
            return False

        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    if dfs(i, j):
                        return True
        return False
