class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        INF = 10**6
        def f(u):
            dist = [INF] * n
            dist[u] = 0
            while u != -1:
                v = edges[u]
                if v == -1 or dist[v] != INF:
                    break
                dist[v] = dist[u] + 1
                u = v
            return dist
        
        dist1 = f(node1)
        dist2 = f(node2)

        ans = -1
        mi = INF
        for i in range(n):
            if dist1[i] == INF or dist2[i] == INF:
                continue
            if mi > max(dist1[i], dist2[i]):
                mi = max(dist1[i],dist2[i])
                ans = i
        return ans

