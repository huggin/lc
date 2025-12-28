class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        ans = -float('inf')
        for i in range(n):
            dp[i] = energy[i]
            if i - k >= 0:
                dp[i] = max(dp[i], dp[i-k] + energy[i])
            if i + k >= n:
                ans = max(ans, dp[i])
        return ans
