class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        m = len(queries)
        dp = [n - 1 - i for i in range(n)]
        ans = []

        prev = [[] for _ in range(n)]
        for i in range(1, n):
            prev[i].append(i - 1)

        def dfs(u):
            for w in prev[u]:
                if dp[w] > dp[u] + 1:
                    dp[w] = dp[u] + 1
                    dfs(w)

        for u, v in queries:
            prev[v].append(u)
            dp[u] = min(dp[u], dp[v] + 1)
            dfs(u)
            ans.append(dp[0])
        return ans
