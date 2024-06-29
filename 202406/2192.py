class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        topo = []
        g = [[] for _ in range(n)]
        gr = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            gr[j].append(i)

        v = [0] * n

        def dfs(u):
            v[u] = 1
            for w in g[u]:
                if v[w] == 0:
                    dfs(w)
            v[u] = 2
            topo.append(u)

        for u in range(n):
            if v[u] == 0:
                dfs(u)

        ans = [set() for _ in range(n)]
        for u in reversed(topo):
            for v in gr[u]:
                for w in ans[v]:
                    ans[u].add(w)
                ans[u].add(v)

        return [sorted(list(c)) for c in ans]
