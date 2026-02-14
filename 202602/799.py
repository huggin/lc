class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for _ in range(101)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(query_row + 1):
                if dp[i][j] > 1:
                    half = (dp[i][j] - 1) / 2
                    dp[i + 1][j] += half
                    dp[i + 1][j + 1] += half
        return 1 if dp[query_row][query_glass] >= 1 else dp[query_row][query_glass]
