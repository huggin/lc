from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        if grid[0][0] == 1:
            return -1

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        q.append((0, 0, 1))
        grid[0][0] = 1
        while q:
            x, y, d = q.popleft()
            if x == n - 1 and y == n - 1:
                return d
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and grid[nx][ny] == 0:
                    q.append((nx, ny, d + 1))
                    grid[nx][ny] = 1

        return -1
