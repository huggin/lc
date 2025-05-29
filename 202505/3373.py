class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            return g

        g1 = build(edges1)
        g2 = build(edges2)

        dist1 = [0] * (len(edges1) + 1)
        dist2 = [0] * (len(edges2) + 1)
        
        def dfs(g, dist, u, p=-1, d=0):
            dist[u] = d
            for v in g[u]:
                if v == p:
                    continue
                dfs(g, dist, v, u, 1-d)

        dfs(g1, dist1, 0, -1, 0)
        dfs(g2, dist2, 0, -1, 0)
        a = sum(dist2)
        b = len(dist2) - a
        ma = max(a, b)
        ans = [ma] * (len(edges1) + 1)
        a = sum(dist1)
        b = len(dist1) - a
        for i in range(len(edges1)+1):
            if dist1[i] == 0:
                ans[i] += b
            else:
                ans[i] += a
        return ans
            
