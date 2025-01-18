class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        v = [[-1] * m for _ in range(n)]
        pq = []
        heapq.heappush(pq, (0, 0, 0))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while pq:
            w, i, j = heapq.heappop(pq)
            if v[i][j] != -1:
                continue
            v[i][j] = w
            for k in range(4):
                nw = w
                if k != grid[i][j] - 1:
                    nw = w + 1
                ni = i + dx[k]
                nj = j + dy[k]
                if ni >= 0 and ni < n and nj >= 0 and nj < m:
                    heapq.heappush(pq, (nw, ni, nj))

        return v[n - 1][m - 1]
