import math


class Solution:
    def solve(self, a, n, mask, k):
        if mask == 0:
            return 0
        if mask in self.dp:
            return self.dp[mask]
        ans = 0
        for i in range(n):
            if mask & (1 << i) == 0:
                continue
            for j in range(i + 1, n):
                if mask & (1 << j) == 0:
                    continue
                ans = max(
                    ans,
                    k * math.gcd(a[i], a[j])
                    + self.solve(a, n, mask & ~(1 << i) & ~(1 << j), k + 1),
                )

        self.dp[mask] = ans
        return ans

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        mask = (1 << n) - 1
        self.dp = {}
        return self.solve(nums, n, mask, 1)
