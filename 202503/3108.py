class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        visited = [-1] * n
        group = 0
        q = deque()
        av = []
        for u in range(n):
            if visited[u] == -1:
                curr = (1 << 31) - 1
                visited[u] = group
                q.append(u)
                while len(q) > 0:
                    x = q.popleft()
                    for y, w in g[x]:
                        curr &= w
                        if visited[y] == -1:
                            visited[y] = group
                            q.append(y)
                av.append(curr)
                group += 1

        ans = [-1] * len(query)
        for k, (s, t) in enumerate(query):
            if visited[s] == visited[t]:
                ans[k] = av[visited[s]]
        return ans
