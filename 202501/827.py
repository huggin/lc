class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        v = [[0] * n for _ in range(n)]
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        ans = 0
        idx = 1
        d = {}
        q = deque()
        for i in range(n):
            for j in range(n):
                if v[i][j] == 0 and grid[i][j] == 1:
                    cnt = 0
                    q.append((i, j))
                    v[i][j] = idx
                    while q:
                        x, y = q.popleft()
                        cnt += 1
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if (
                                nx >= 0
                                and nx < n
                                and ny >= 0
                                and ny < n
                                and v[nx][ny] == 0
                                and grid[nx][ny] == 1
                            ):
                                v[nx][ny] = idx
                                q.append((nx, ny))
                    d[idx] = cnt
                    idx += 1
                    ans = max(ans, cnt)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt = 1
                    color = set()
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if (
                            ni >= 0
                            and ni < n
                            and nj >= 0
                            and nj < n
                            and grid[ni][nj] == 1
                            and v[ni][nj] not in color
                        ):
                            cnt += d[v[ni][nj]]
                            color.add(v[ni][nj])
                    ans = max(ans, cnt)
        return ans
