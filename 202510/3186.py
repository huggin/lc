class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        C = Counter(power)
        power = sorted(set(power))
        n = len(power)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = power[0] * C[power[0]]

        for i in range(1, n):
            dp[0][i] = power[i] * C[power[i]]
            j = i - 1
            while j >= 0 and power[j] + 2 >= power[i]:
                j -= 1
            if j >= 0:
                dp[0][i] += max(dp[0][j], dp[1][j])
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])

        return max(dp[0])
