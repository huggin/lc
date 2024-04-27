class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(key)
        m = len(ring)
        oo = 10000
        dp = [[oo for _ in range(m)] for _ in range(n)]
        for i in range(m):
            if ring[i] == key[0]:
                dp[0][i] = min(i, m - i) + 1

        for j in range(1, n):
            for i in range(m):
                if key[j] == ring[i]:
                    for k in range(m):
                        if i <= k:
                            dp[j][i] = min(
                                dp[j][i], dp[j - 1][k] + min(k - i, i + m - k) + 1
                            )
                        else:
                            dp[j][i] = min(
                                dp[j][i], dp[j - 1][k] + min(i - k, k + m - i) + 1
                            )

        return min(dp[n - 1])
