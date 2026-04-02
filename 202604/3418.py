class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])
        dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        else:
            dp[0][0][1] = dp[0][0][0]
        dp[0][0][2] = dp[0][0][1]
        for i in range(1, n):
            if coins[i][0] >= 0:
                dp[i][0][0] = dp[i-1][0][0] + coins[i][0]
                dp[i][0][1] = dp[i-1][0][1] + coins[i][0]
                dp[i][0][2] = dp[i-1][0][2] + coins[i][0]
            else:
                dp[i][0][0] = dp[i-1][0][0] + coins[i][0]
                dp[i][0][1] = max(dp[i-1][0][1] + coins[i][0], dp[i-1][0][0])
                dp[i][0][2] = max(dp[i-1][0][2] + coins[i][0], dp[i-1][0][1])
        for j in range(1, m):
            if coins[0][j] >= 0:
                dp[0][j][0] = dp[0][j-1][0] + coins[0][j]
                dp[0][j][1] = dp[0][j-1][1] + coins[0][j]
                dp[0][j][2] = dp[0][j-1][2] + coins[0][j]
            else:
                dp[0][j][0] = dp[0][j-1][0] + coins[0][j]
                dp[0][j][1] = max(dp[0][j-1][1] + coins[0][j], dp[0][j-1][0])
                dp[0][j][2] = max(dp[0][j-1][2] + coins[0][j], dp[0][j-1][1])
        
        for i in range(1, n):
            for j in range(1, m):
                if coins[i][j] >= 0:
                    dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j][0]) + coins[i][j]
                    dp[i][j][1] = max(dp[i][j-1][1], dp[i-1][j][1]) + coins[i][j]
                    dp[i][j][2] = max(dp[i][j-1][2], dp[i-1][j][2]) + coins[i][j]
                else:
                    dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j][0]) + coins[i][j]
                    dp[i][j][1] = max(max(dp[i][j-1][1], dp[i-1][j][1]) + coins[i][j], dp[i-1][j][0], dp[i][j-1][0])
                    dp[i][j][2] = max(max(dp[i][j-1][2], dp[i-1][j][2]) + coins[i][j], dp[i-1][j][1], dp[i][j-1][1])
        
        return dp[n-1][m-1][2]

