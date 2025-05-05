class Solution:
    def numTilings(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2

        M = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % M

        return dp[n]
