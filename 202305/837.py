class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        total = [0] * (n + 1)
        total[0] = dp[0]
        d = 1 / maxPts
        for i in range(1, n + 1):
            dp[i] = total[i - 1] * d
            if i < k:
                total[i] = total[i - 1] + dp[i]
            else:
                total[i] = total[i - 1]
            if i >= maxPts:
                total[i] = max(0, total[i] - dp[i - maxPts])

        print(dp)
        print(total)

        ans = 0
        for i in range(k, n + 1):
            ans += dp[i]
        return ans
