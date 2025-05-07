class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = []
        heapq.heappush(pq, (0, 0, 0))

        n = len(moveTime)
        m = len(moveTime[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        dist = [[int(1e10) for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        while len(pq) > 0:
            d, i, j = heapq.heappop(pq)
            if d > dist[i][j]:
                continue
            dist[i][j] = d
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                td = max(d, moveTime[ni][nj]) + 1
                if td < dist[ni][nj]:
                    dist[ni][nj] = td
                    heapq.heappush(pq, (td, ni, nj))

        return dist[n - 1][m - 1]
