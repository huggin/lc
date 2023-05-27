from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        first = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if first:
                        first = False
                        grid[i][j] = 2
                        q.append((i, j))
                        while len(q) > 0:
                            x, y = q.popleft()
                            for k in range(4):
                                nx = x + dx[k]
                                ny = y + dy[k]
                                if not (
                                    nx >= 0
                                    and nx < n
                                    and ny >= 0
                                    and ny < m
                                    and grid[nx][ny] == 1
                                ):
                                    continue
                                q.append((nx, ny))
                                grid[nx][ny] = 2
                    else:
                        q.append((i, j, 0))

        while len(q) > 0:
            x, y, d = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                    continue
                if grid[nx][ny] == 1:
                    continue
                elif grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    q.append((nx, ny, d + 1))
                else:
                    return d

        return -1
