class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        g = [[] for _ in range(n)]
        for i, e in enumerate(edges):
            g[e[0]].append((e[1], i))
            g[e[1]].append((e[0], i))

        pq = [(-1, start_node)]
        dest = [0] * n
        dest[start_node] = 1
        while pq:
            w, u = heapq.heappop(pq)
            w = -w
            if dest[u] > w:
                continue
            for v, i in g[u]:
                if dest[v] < w * succProb[i]:
                    dest[v] = w * succProb[i]
                    heapq.heappush(pq, (-dest[v], v))

        return dest[end_node]
