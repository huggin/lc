from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        n = len(grid)
        m = len(grid[0])
        ans = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] = 1
                    q.append((i, j))
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if (
                                nx >= 0
                                and nx < n
                                and ny >= 0
                                and ny < m
                                and grid[nx][ny] == "1"
                            ):
                                q.append((nx, ny))
                                grid[nx][ny] = 1

        return ans
