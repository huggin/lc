class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u-1].append(v-1)
            g[v-1].append(u-1)

        q = deque()
        q.append((0, 0))
        dist = [[] for _ in range(n)]
        dist[0].append(0)
        while len(q) > 0:
            u, t = q.popleft()
            for v in g[u]:
                if len(dist[v]) < 2 or dist[v][-1] == dist[v][-2]:
                    q.append((v, len(dist[v])))
                    dist[v].append(dist[u][t] + 1)
        ans = 0
        for i in range(dist[n-1][-1]):
            ans += time
            if i != dist[n-1][-1]-1 and ans // change % 2 == 1:
                ans = (ans + change) // change * change
        return ans


