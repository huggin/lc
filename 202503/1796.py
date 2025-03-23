class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        M = 10**9 + 7
        g = [[] for _ in range(n)]
        for u, v, time in roads:
            g[u].append((v, time))
            g[v].append((u, time))

        pq = []
        dist = [-1] * n
        cnt = [0] * n
        heapq.heappush(pq, (0, 0, -1))
        while pq:
            w, u, c = heapq.heappop(pq)
            if dist[n - 1] != -1 and w > dist[n - 1]:
                break
            if dist[u] == -1:
                dist[u] = w
                cnt[u] = 1 if c == -1 else cnt[c]
            elif dist[u] == w:
                cnt[u] += cnt[c]
                continue
            elif dist[u] < w:
                continue

            for v, t in g[u]:
                if dist[v] == -1:
                    heapq.heappush(pq, (w + t, v, u))

        return cnt[n - 1] % M
