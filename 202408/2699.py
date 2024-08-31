class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            g[u].append((v, i))
            g[v].append((u, i))

        pq = [(0, source)]
        desto = [-1] * n

        while len(pq) > 0:
            cw, u = heapq.heappop(pq)
            if desto[u] != -1:
                continue
            desto[u] = cw
            for v, i in g[u]:
                w = edges[i][2]
                if w == -1:
                    w = 1
                heapq.heappush(pq, (desto[u] + w, v))

        if desto[destination] != -1 and desto[destination] > target:
            return []

        more = target - desto[destination]

        pq = [(0, source)]
        dest = [-1] * n
        while len(pq) > 0:
            cw, u = heapq.heappop(pq)
            if dest[u] != -1:
                continue
            dest[u] = cw
            for v, i in g[u]:
                w = edges[i][2]
                if w == -1:
                    w = 1
                if edges[i][2] == -1:
                    nw = more + desto[v] - dest[u]
                    if nw > w:
                        edges[i][2] = w = nw

                heapq.heappush(pq, (dest[u] + w, v))
        if dest[destination] != -1 and dest[destination] < target:
            return []

        for e in edges:
            if e[2] == -1:
                e[2] = 1

        return edges
