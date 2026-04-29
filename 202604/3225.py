class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        dp = [[0 for _ in range(105)] for _ in range(105)]
        dp2 = [[0 for _ in range(105)] for _ in range(105)]
        ps = [[0 for _ in range(105)] for _ in range(105)]
        p1 = [0] * 105
        p2 = [0] * 105
        for i in range(n):
            for j in range(n):
                ps[i + 1][j] = ps[i][j] + grid[i][j]

        for i1 in range(n + 1):
            for i2 in range(n + 1):
                if i1 > i2:
                    dp[i1][i2] = ps[i1][1] - ps[i2][1]
                elif i1 < i2:
                    dp[i1][i2] = ps[i2][0] - ps[i1][0]

        for j in range(2, n):
            for i in range(n + 1):
                for k in range(n + 1):
                    dp2[i][k] = dp[i][k]
            for i1 in range(n + 1):
                m1, m2 = 0, 0
                for i0 in range(i1 + 1):
                    m1 = max(m1, dp2[i0][i1])
                for i0 in range(n + 1):
                    m2 = max(m2, dp2[i0][i1])
                p1[i1] = 0
                for i0 in range(i1 + 1, n + 1):
                    p1[i0] = max(p1[i0 - 1], dp2[i0][i1] - ps[i0][j - 1])
                p2[n + 1] = 0
                for i0 in range(n, i1 - 1, -1):
                    p2[i0] = max(p2[i0 + 1], dp2[i0][i1])
                for i2 in range(n + 1):
                    if i1 >= i2:
                        dp[i1][i2] = m2 + ps[i1][j] - ps[i2][j]
                    else:
                        dp[i1][i2] = m1 + ps[i2][j - 1] - ps[i1][j - 1]
                        dp[i1][i2] = max(dp[i1][i2], p1[i2] + ps[i2][j - 1])
                        dp[i1][i2] = max(dp[i1][i2], p2[i2])

        ans = 0
        for r in dp:
            for i in r:
                ans = max(ans, i)
        return ans
