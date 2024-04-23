class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        t = [[] for _ in range(n)]
        for u, v in edges:
            t[u].append(v)
            t[v].append(u)

        ans = set()
        q = deque()
        dest = [-1] * n
        dest[0] = 0
        q.append(0)

        while len(q) > 0:
            u = q.popleft()
            for v in t[u]:
                if dest[v] == -1:
                    dest[v] = dest[u] + 1
                    q.append(v)
        ma = max(dest)
        v = -1
        for u in range(n):
            if dest[u] == ma:
                v = u
                break

        dest = [-1] * n
        dest[v] = 0
        q.append(v)
        prev = [-1] * n
        while len(q) > 0:
            u = q.popleft()
            for v in t[u]:
                if dest[v] == -1:
                    dest[v] = dest[u] + 1
                    prev[v] = u
                    q.append(v)

        ma = max(dest)
        for u in range(n):
            if dest[u] == ma:
                v = u
                while prev[v] != -1:
                    if dest[v] == ma // 2 or ma % 2 == 1 and dest[v] == ma // 2 + 1:
                        ans.add(v)
                    v = prev[v]

        return list(ans)
