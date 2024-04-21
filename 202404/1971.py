class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [0] * n
        q = deque()
        q.append(source)
        visited[source] = 1
        while len(q) > 0:
            u = q.popleft()
            for v in g[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    q.append(v)

        return visited[destination]
