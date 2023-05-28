class Solution:
    def solve(self, a, i, j, left, right):
        if i > j or left > right:
            return 0
        if i == j:
            return right - left
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        ans = 100000000
        for k in range(i, j + 1):
            ans = min(
                ans,
                right
                - left
                + self.solve(a, i, k - 1, left, a[k])
                + self.solve(a, k + 1, j, a[k], right),
            )
        self.dp[i][j] = ans
        return ans

    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts.sort()
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(m + 1)]
        return self.solve(cuts, 0, m - 1, 0, n)
