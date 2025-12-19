class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        ans = []
        g = [[] for _ in range(n)]
        for u, v, t in meetings:
            g[u].append((t, v))
            g[v].append((t, u))

        visited = [0] * n
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))
        while pq:
            time, u = heappop(pq)
            if visited[u] == 1:
                continue
            ans.append(u)
            visited[u] = 1
            for t, v in g[u]:
                if t >= time:
                    heappush(pq, (t, v))
        return ans
