class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        def f(i, j):
            q = deque()
            q.append((i, j))
            ans = 1
            while len(q) > 0:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (
                        nx < 0
                        or nx >= n
                        or ny < 0
                        or ny >= m
                        or visited[nx][ny] == 1
                        or grid2[nx][ny] == 0
                    ):
                        continue
                    visited[nx][ny] = 1
                    if grid1[nx][ny] == 0:
                        ans = 0
                    q.append((nx, ny))
            return ans

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    ans += f(i, j)

        return ans
