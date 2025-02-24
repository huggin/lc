class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(amount)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        q = deque()
        q.append(0)
        v = [0] * n
        v[0] = 1
        prev = [-1] * n
        leaf = set()
        while q:
            u = q.popleft()
            isleaf = True
            for w in g[u]:
                if v[w] == 0:
                    isleaf = False
                    v[w] = 1
                    prev[w] = u
                    q.append(w)
            if isleaf:
                leaf.add(u)

        path = []
        while bob != -1:
            path.append(bob)
            bob = prev[bob]

        for i in range(len(path) // 2):
            amount[path[i]] = 0
        if len(path) & 1:
            amount[path[len(path) // 2]] //= 2

        v = [0] * n
        d = [-1] * n
        v[0] = 1
        d[0] = amount[0]
        q.append(0)
        while q:
            u = q.popleft()
            for w in g[u]:
                if v[w] == 0:
                    d[w] = d[u] + amount[w]
                    v[w] = 1
                    q.append(w)

        ans = -float("inf")
        for i in range(n):
            if i in leaf:
                ans = max(ans, d[i])
        return ans
