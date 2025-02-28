class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        i, j = m, n
        ans = []
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j]:
                ans.append(s1[i - 1])
                i -= 1
            else:
                ans.append(s2[j - 1])
                j -= 1

        while i > 0:
            ans.append(s1[i - 1])
            i -= 1
        while j > 0:
            ans.append(s2[j - 1])
            j -= 1
        return "".join(reversed(ans))
