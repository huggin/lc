from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])

        dist = [[[-1 for _ in range(64)] for _ in range(m)] for _ in range(n)]
        q = deque()
        mask = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    q.append((i, j, 0))
                    dist[i][j][0] = 0
                elif grid[i][j].islower():
                    mask |= 1 << ord(grid[i][j]) - ord("a")

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        while q:
            x, y, key = q.popleft()
            d = dist[x][y][key]
            if key == mask:
                return d
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                    continue
                if grid[nx][ny] == "#":
                    continue

                c = grid[nx][ny]
                if c == "." or c == "@":
                    if dist[nx][ny][key] != -1:
                        continue
                    dist[nx][ny][key] = d + 1
                    q.append((nx, ny, key))
                elif c.islower():
                    key2 = key | 1 << (ord(c) - ord("a"))
                    if dist[nx][ny][key2] != -1:
                        continue
                    dist[nx][ny][key2] = d + 1
                    q.append((nx, ny, key2))
                elif c.isupper() and key & (1 << (ord(c) - ord("A"))):
                    if dist[nx][ny][key] != -1:
                        continue
                    dist[nx][ny][key] = d + 1
                    q.append((nx, ny, key))

        return -1
