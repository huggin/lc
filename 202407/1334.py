class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        g = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        for i in range(n):
            g[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (
                        (g[i][j] == -1 or g[i][j] > g[i][k] + g[k][j])
                        and g[i][k] != -1
                        and g[k][j] != -1
                    ):
                        g[i][j] = g[i][k] + g[k][j]

        ans = -1
        ma = n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if g[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= ma:
                ma = cnt
                ans = i
        return ans
