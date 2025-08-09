class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))
        for i in range(n):
            fruits[i][i] = 0
        dp = [[0] * n for _ in range(n)]
        dp[0][n-1] = fruits[0][n-1]
        dp[n-1][0] = fruits[n-1][0]

        for i in range(1, n-1):
            for j in range(max(n-1-i, i+1), n):
                dp[i][j] = dp[i-1][j]
                if j > i:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1])
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1])
                dp[i][j] += fruits[i][j]
        
        for j in range(1, n-1):
            for i in range(max(n-1-j, j+1), n):
                dp[i][j] = dp[i][j-1]
                if i > j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1])
                if i + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1])
                dp[i][j] += fruits[i][j]

        return ans + dp[n-1][n-2] + dp[n-2][n-1]
