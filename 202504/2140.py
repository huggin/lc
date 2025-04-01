class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = max(questions[i][0], dp[i + 1])
            if i + 1 + questions[i][1] < n:
                dp[i] = max(dp[i], questions[i][0] + dp[i + 1 + questions[i][1]])

        return dp[0]
