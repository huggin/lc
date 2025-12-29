class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[-inf] * 3 for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][0] = 0

        for p in prices:
            for i in range(k, 0, -1):
                dp[i][0] = max(dp[i][0], dp[i][1] - p, dp[i][2] + p)
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + p)
                dp[i][2] = max(dp[i][2], dp[i - 1][0] - p)

        return dp[k][0]
