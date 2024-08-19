class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[1] = 0
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for i in range(2, n + 1):
            for a in p:
                if i % a == 0:
                    dp[i] = min(dp[i], dp[i // a] + a)

        return dp[n]
