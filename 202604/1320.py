class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        dp = [[[float("inf")] * (26) for _ in range(26)] for _ in range(n + 1)]
        for i in range(26):
            for j in range(i, 26):
                dp[0][i][j] = 0

        for k in range(n):
            idx = ord(word[k]) - ord("A")
            x, y = idx // 6, idx % 6
            for i in range(26):
                x1, y1 = i // 6, i % 6
                for j in range(i, 26):
                    x2, y2 = j // 6, j % 6
                    dp[k + 1][min(idx, j)][max(idx, j)] = min(
                        dp[k + 1][min(idx, j)][max(idx, j)],
                        dp[k][i][j] + abs(x1 - x) + abs(y1 - y),
                    )
                    dp[k + 1][min(idx, i)][max(idx, i)] = min(
                        dp[k + 1][min(idx, i)][max(idx, i)],
                        dp[k][i][j] + abs(x2 - x) + abs(y2 - y),
                    )

        ans = float("inf")
        for i in range(26):
            for j in range(i, 26):
                ans = min(ans, dp[n][i][j])
        return ans
