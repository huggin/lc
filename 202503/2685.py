class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        visit = [0] * n

        def dfs(u, group):
            group.add(u)
            visit[u] = 1
            for v in g[u]:
                if visit[v] == 0:
                    dfs(v, group)

        for i in range(n):
            if visit[i] == 0:
                group = set()
                dfs(i, group)
                k = len(group) - 1
                flag = True
                for u in group:
                    if len(g[u]) != k:
                        flag = False
                        break

                if flag:
                    ans += 1
        return ans
