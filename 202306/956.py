class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods)
        len(rods)
        dp = [-1 for _ in range(s + 1)]

        dp[0] = 0

        for a in rods:
            dp2 = dp.copy()
            for i in range(s + 1):
                if dp2[i] < 0 or i + a > s:
                    continue
                dp[i + a] = max(dp[i + a], dp2[i])
                dp[abs(i - a)] = max(dp[abs(i - a)], dp2[i] + min(i, a))

        return dp[0]
