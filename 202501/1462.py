class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 1
        for a, b in prerequisites:
            g[a][b] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = max(g[i][j], g[i][k] * g[k][j])

        ans = [False] * len(queries)
        for k, q in enumerate(queries):
            ans[k] = True if g[q[0]][q[1]] else False
        return ans
