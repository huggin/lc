class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        M = int(1e9 + 7)

        dp = [0] * (n + 1)
        dp[0] = 1

        a = []
        for i in range(1, n + 1):
            if i**x <= n:
                a.append(i**x)

        for i in range(len(a)):
            for j in range(n, -1, -1):
                if j - a[i] >= 0:
                    dp[j] = (dp[j] + dp[j - a[i]]) % M

        return dp[n]
