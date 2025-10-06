class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = []
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        n = len(grid)
        m = len(grid[0])
        heappush(pq, (grid[0][0], 0, 0))
        ans = 0
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        while pq:
            v, i, j = heappop(pq)
            ans = max(ans, v)
            if i == n - 1 and j == m - 1:
                break
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni >= 0 and ni < n and nj >= 0 and nj < m and visited[ni][nj] == 0:
                    heappush(pq, (grid[ni][nj], ni, nj))
                    visited[ni][nj] = 1
        return ans

