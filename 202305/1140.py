class Solution:
    def solve2(self, a, n, k, m):
        if k == n:
            return 0

        if self.dp2[k][m] != -1:
            return self.dp2[k][m]

        ans = a[k] - self.solve(a, n, k + 1, max(m, 1))
        total = a[k]
        for i in range(k + 1, min(k + 2 * m, n)):
            total += a[i]
            ans = max(ans, total - self.solve(a, n, i + 1, max(m, i - k + 1)))
        self.dp2[k][m] = ans
        return ans

    def solve(self, a, n, k, m):
        if k == n:
            return 0

        if self.dp[k][m] != -1:
            return self.dp[k][m]

        ans = a[k] - self.solve2(a, n, k + 1, max(m, 1))
        total = a[k]
        for i in range(k + 1, min(k + 2 * m, n)):
            total += a[i]
            ans = max(ans, total - self.solve2(a, n, i + 1, max(m, i - k + 1)))
        self.dp[k][m] = ans
        return ans

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        if n == 1:
            return piles[0]
        self.dp = [[-1 for _ in range(n)] for _ in range(n)]
        self.dp2 = [[-1 for _ in range(n)] for _ in range(n)]
        self.solve(piles, n, 0, 1)
        s = sum(piles)

        return (s + self.dp[0][1]) // 2
