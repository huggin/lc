class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ans = 0
        pq = []
        n = len(heightMap)
        m = len(heightMap[0])
        for i in range(n):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heightMap[i][0] = -1
            heapq.heappush(pq, (heightMap[i][m - 1], i, m - 1))
            heightMap[i][m - 1] = -1
        for j in range(1, m - 1):
            heapq.heappush(pq, (heightMap[0][j], 0, j))
            heightMap[0][j] = -1
            heapq.heappush(pq, (heightMap[n - 1][j], n - 1, j))
            heightMap[n - 1][j] = -1

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        wl = 0
        while len(pq) > 0:
            h, i, j = heapq.heappop(pq)
            wl = max(wl, h)
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if (
                    ni >= 0
                    and ni < n
                    and nj >= 0
                    and nj < m
                    and heightMap[ni][nj] != -1
                ):
                    heapq.heappush(pq, (heightMap[ni][nj], ni, nj))
                    if heightMap[ni][nj] < wl:
                        ans += wl - heightMap[ni][nj]
                    heightMap[ni][nj] = -1

        return ans
