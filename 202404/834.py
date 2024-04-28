class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        t = defaultdict(list)
        for u, v in edges:
            t[v].append(u)
            t[u].append(v)
        dp = [None] * n

        def dfs(u, p):
            a = 0
            total = 1
            for v in t[u]:
                if v == p:
                    continue
                d, c = dfs(v, u)
                a += d + c
                total += c
            dp[u] = (a, total)
            return a, total

        ans[0], _ = dfs(0, -1)

        def dfs2(u, p):
            for v in t[u]:
                if v == p:
                    continue
                ans[v] = ans[u] - dp[v][1] + n - dp[v][1]
                dfs2(v, u)

        dfs2(0, -1)

        return ans
