class Solution:
    def solve2(self, a, k, n):
        if k >= n:
            return 0
        if self.dp2[k] != -1:
            return self.dp2[k]

        ans = a[k] - self.solve(a, k + 1, n)
        curr = a[k]
        for i in range(k + 1, min(n, k + 3)):
            curr += a[i]
            ans = max(ans, curr - self.solve(a, i + 1, n))

        self.dp2[k] = ans
        return ans

    def solve(self, a, k, n):
        if k >= n:
            return 0
        if self.dp[k] != -1:
            return self.dp[k]

        ans = a[k] - self.solve2(a, k + 1, n)
        curr = a[k]
        for i in range(k + 1, min(n, k + 3)):
            curr += a[i]
            ans = max(ans, curr - self.solve2(a, i + 1, n))

        self.dp[k] = ans
        return ans

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        self.dp = [-1] * n
        self.dp2 = [-1] * n
        s = sum(stoneValue)
        ans = self.solve(stoneValue, 0, n)
        print(ans)

        alice = (s + ans) / 2
        bob = (s - ans) / 2
        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"

        return "Tie"
