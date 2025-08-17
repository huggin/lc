class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        total =[0] * (n + 1)
        total[0] = dp[0]
        d = 1 / maxPts
        for i in range(1, n+1):
            dp[i] = total[i-1] * d
            total[i] = total[i-1]
            if i < k:
                total[i] += dp[i]
            if i >= maxPts:
                total[i] = max(0, total[i]-dp[i-maxPts])

        return sum(dp[k:n+1])
                

