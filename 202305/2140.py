class Solution:
    def solve(self, a, n, k):
        if k >= n:
            return 0
        if self.dp[k] != -1:
            return self.dp[k]

        ans = self.solve(a, n, k + 1)
        ans = max(ans, a[k][0] + self.solve(a, n, k + 1 + a[k][1]))
        self.dp[k] = ans
        return ans

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        self.dp = [-1] * n
        return self.solve(questions, n, 0)
