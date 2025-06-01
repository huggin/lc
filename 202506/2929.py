class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 < n:
            return 0

        ans = 0
        for i in range(0, min(n, limit) + 1):
            ans += max(0, min(limit, n - i) - max(0, n-i-limit) + 1)
        return ans
