import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        adj = [[] for _ in range(n)]
        m = len(edges)
        for i in range(m):
            v, w = edges[i][0], edges[i][1]
            r = succProb[i]
            adj[v].append((w, r))
            adj[w].append((v, r))

        dist = [0] * n
        dist[start] = 1
        marked = [0] * n
        pq = []
        heapq.heappush(pq, (-1, start))
        while pq:
            curr, v = heapq.heappop(pq)
            if marked[v] == 1:
                continue
            dist[v] = max(-curr, dist[v])
            marked[v] = 1
            for w, r in adj[v]:
                if marked[w] == 0:
                    heapq.heappush(pq, (curr * r, w))

        return dist[end]
