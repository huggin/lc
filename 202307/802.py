from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vadj = [set() for _ in range(n)]
        deg = [0] * n

        q = deque()
        for v in range(n):
            deg[v] = len(graph[v])
            for w in graph[v]:
                vadj[w].add(v)

        for v in range(n):
            if deg[v] == 0:
                q.append(v)

        ans = []
        while q:
            v = q.popleft()
            ans.append(v)
            for w in vadj[v]:
                deg[w] -= 1
                if deg[w] == 0:
                    q.append(w)

        return sorted(ans)
