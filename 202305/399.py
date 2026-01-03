from collections import deque


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        v2i = {}
        n = len(equations)
        adj = []
        vertex = []

        for i in range(n):
            idx1 = -1
            if equations[i][0] not in v2i:
                vertex.append(equations[i][0])
                adj.append([])
                idx1 = len(vertex) - 1
                v2i[equations[i][0]] = idx1
            else:
                idx1 = v2i[equations[i][0]]

            idx2 = -1
            if equations[i][1] not in v2i:
                vertex.append(equations[i][1])
                adj.append([])
                idx2 = len(vertex) - 1
                v2i[equations[i][1]] = idx2
            else:
                idx2 = v2i[equations[i][1]]

            adj[idx1].append((idx2, values[i]))
            adj[idx2].append((idx1, 1 / values[i]))

        m = len(vertex)
        ans = []
        for q in queries:
            if q[0] not in v2i or q[1] not in v2i:
                ans.append(-1)
            else:
                src = v2i[q[0]]
                dst = v2i[q[1]]
                dist = [-1] * m
                dist[src] = 1
                q = deque()
                q.append(src)
                while len(q) > 0:
                    v = q.popleft()
                    for w, d in adj[v]:
                        if dist[w] == -1:
                            q.append(w)
                            dist[w] = dist[v] * d

                ans.append(dist[dst])

        return ans
