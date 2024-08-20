class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def f(k, m, ab):
            if k == n:
                return 0
            ans = -float("inf")
            curr = 0
            for i in range(k, min(k + 2 * m, n)):
                curr += piles[i]
                ans = max(ans, curr - f(i + 1, max(m, i - k + 1), 1 - ab))

            return ans

        return (f(0, 1, 0) + sum(piles)) // 2
