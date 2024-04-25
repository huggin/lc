class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        dp[ord(s[0]) - ord("a")] = 1
        for i in range(1, n):
            d = ord(s[i]) - ord("a")
            dp[d] += 1
            for j in range(max(0, d - k), min(25, k + d) + 1):
                if j == d:
                    continue
                dp[d] = max(dp[d], dp[j] + 1)

        return max(dp)
