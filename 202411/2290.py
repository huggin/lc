class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append((0, 0))
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        m = len(grid)
        n = len(grid[0])
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        visited[0][0] = 0

        while q:
            i, j = q.popleft()
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] != -1:
                    continue
                if grid[x][y] == 0:
                    visited[x][y] = visited[i][j]
                    q.appendleft((x, y))
                else:
                    visited[x][y] = visited[i][j] + 1
                    q.append((x, y))

        return visited[m - 1][n - 1]
