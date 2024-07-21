class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        g = [[] for _ in range(k)]
        for a, b in rowConditions:
            g[a - 1].append(b - 1)

        topo = []
        visited = [0] * k

        def dfs(u, topo, g, visited):
            visited[u] = 1
            for v in g[u]:
                if visited[v] == 1:
                    return
                elif visited[v] == 0:
                    dfs(v, topo, g, visited)
            visited[u] = 2
            topo.append(u)

        for i in range(k):
            if visited[i] == 0:
                dfs(i, topo, g, visited)

        g2 = [[] for _ in range(k)]
        for a, b in colConditions:
            g2[a - 1].append(b - 1)

        topo2 = []
        visited = [0] * k

        for i in range(k):
            if visited[i] == 0:
                dfs(i, topo2, g2, visited)

        if len(topo) != k or len(topo2) != k:
            return []
        topo.reverse()
        topo2.reverse()

        ans = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            idx = topo.index(i)
            jdx = topo2.index(i)
            ans[idx][jdx] = i + 1

        return ans
