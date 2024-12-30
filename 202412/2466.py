class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        M = int(1e9 + 7)
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % M
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % M

        for i in range(low, high + 1):
            ans = (ans + dp[i]) % M

        return ans
