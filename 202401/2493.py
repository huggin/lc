class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        v = [-1] * n
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)

        ans = 0
        for u in range(n):
            if v[u] == -1:
                q = deque()
                q.append((u, 0))
                v[u] = 0
                l = u
                group = []
                while q:
                    x, d = q.popleft()
                    group.append(x)
                    l = x
                    for y in g[x]:
                        if v[y] == -1:
                            v[y] = d + 1
                            q.append((y, d + 1))
                        elif v[y] == d + 1 or v[y] == d - 1:
                            continue
                        else:
                            return -1
                mx = 1
                for x in group:
                    v2 = [0] * n
                    q.append((x, 1))
                    v2[x] = 1
                    while q:
                        m = len(q)
                        for _ in range(m):
                            x, d = q.popleft()
                            mx = max(mx, d)
                            for y in g[x]:
                                if v2[y] == 0:
                                    q.append((y, d + 1))
                                    v2[y] = 1
                ans += mx

        return ans
