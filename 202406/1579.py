class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.cnt = [0] * n
        self.edges = 0

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        self.edges += 1
        if self.cnt[pu] < self.cnt[pv]:
            self.parent[pu] = pv
            self.cnt[pv] += self.cnt[pu]
            return pv
        else:
            self.parent[pv] = pu
            self.cnt[pu] += self.cnt[pv]
            return pu

    def getEdges(self):
        return self.edges


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)

        dj1 = DisjointSet(n + 1)
        dj2 = DisjointSet(n + 1)
        ans = 0
        for op, u, v in edges:
            if op == 3:
                pu = dj1.find(u)
                pv = dj1.find(v)
                if pu == pv:
                    ans += 1
                else:
                    dj1.union(pu, pv)
                    dj2.union(pu, pv)
            elif op == 2:
                pu = dj2.find(u)
                pv = dj2.find(v)
                if pu == pv:
                    ans += 1
                else:
                    dj2.union(pu, pv)
            else:
                pu = dj1.find(u)
                pv = dj1.find(v)
                if pu == pv:
                    ans += 1
                else:
                    dj1.union(pu, pv)

        return ans if dj1.getEdges() == n - 1 and dj2.getEdges() == n - 1 else -1
