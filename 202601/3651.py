class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        a = []
        for i in range(n):
            for j in range(m):
                a.append((grid[i][j], i, j))
        a.sort()

        MAX_V = float("inf")

        dp = [[[MAX_V] * (k + 1) for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        for kk in range(k + 1):
            for i in range(n):
                for j in range(m):
                    if dp[i][j][kk] == MAX_V:
                        continue
                    if j + 1 < m:
                        dp[i][j + 1][kk] = min(
                            dp[i][j + 1][kk], dp[i][j][kk] + grid[i][j + 1]
                        )
                    if i + 1 < n:
                        dp[i + 1][j][kk] = min(
                            dp[i + 1][j][kk], dp[i][j][kk] + grid[i + 1][j]
                        )
            if kk < k:
                i = len(a) - 1
                curr = MAX_V
                j = i
                while j >= 0:
                    while j >= 0 and grid[a[i][1]][a[i][2]] == grid[a[j][1]][a[j][2]]:
                        curr = min(curr, dp[a[j][1]][a[j][2]][kk])
                        j -= 1
                    for idx in range(j + 1, i + 1):
                        dp[a[idx][1]][a[idx][2]][kk + 1] = min(
                            dp[a[idx][1]][a[idx][2]][kk + 1], curr
                        )
                    i = j

        return min(dp[n - 1][m - 1])
