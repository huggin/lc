class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m = len(grid)
        n = len(grid[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        v = [[-1 for _ in range(n)] for _ in range(m)]
        v[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        while pq:
            w, x, y = heapq.heappop(pq)

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or v[nx][ny] != -1:
                    continue

                if grid[nx][ny] <= w + 1:
                    v[nx][ny] = w + 1
                elif (grid[nx][ny] - w) % 2 == 1:
                    v[nx][ny] = grid[nx][ny]
                else:
                    v[nx][ny] = grid[nx][ny] + 1
                heapq.heappush(pq, (v[nx][ny], nx, ny))

        return v[m - 1][n - 1]
