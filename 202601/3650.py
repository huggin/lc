class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))

        pq = []
        dist = [inf] * n
        dist[0] = 0
        heappush(pq, (0, 0))
        while pq:
            d, u = heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u]:
                continue
            dist[u] = d
            for v, w in g[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heappush(pq, (d + w, v))

        return -1
