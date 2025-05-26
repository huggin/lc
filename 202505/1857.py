class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g2[v].append(u)

        vis = [0] * n
        topo = []
        def dfs(u):
            vis[u] = 1
            for v in g[u]:
                if vis[v] == 0:
                    if not dfs(v):
                        return False
                elif vis[v] == 1:
                    return False
            vis[u] = 2
            topo.append(u)
            return True
        
        for i in range(n):
            if vis[i] == 0:
                if not dfs(i):
                    return -1
        
        ans = 0
        cnt = [[0] * 26 for _ in range(n)]
        for u in reversed(topo):
            for v in g2[u]:
                for j in range(26):
                    cnt[u][j] = max(cnt[u][j], cnt[v][j])
            cnt[u][ord(colors[u]) - ord('a')] += 1
            ans = max(ans, cnt[u][ord(colors[u]) - ord('a')])
        return ans

