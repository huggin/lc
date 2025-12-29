class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = [i for i in range(c + 1)]
        size = [1] * (c + 1)

        def id(u):
            while u != parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            if size[u] < size[v]:
                parent[u] = v
                size[v] += size[u]
            else:
                parent[v] = u
                size[u] += size[v]

        for u, v in connections:
            ui = id(u)
            vi = id(v)
            if ui != vi:
                union(ui, vi)

        i2g = {}
        groups = []
        for i in range(1, c + 1):
            ui = id(i)
            if ui not in i2g:
                groups.append(SortedList())
                i2g[ui] = len(groups) - 1
            groups[i2g[ui]].add(i)

        ans = []
        for q, u in queries:
            if q == 1:
                ui = id(u)
                if u in groups[i2g[ui]]:
                    ans.append(u)
                elif len(groups[i2g[ui]]) == 0:
                    ans.append(-1)
                else:
                    ans.append(groups[i2g[ui]][0])
            else:
                ui = id(u)
                if u in groups[i2g[ui]]:
                    groups[i2g[ui]].pop(groups[i2g[ui]].index(u))
        return ans
