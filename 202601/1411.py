class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [[[[0] * 3 for _ in range(3)] for _ in range(3)] for _ in range(n)]
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                for k in range(3):
                    if j == k:
                        continue
                    dp[0][i][j][k] = 1
        for idx in range(1, n):
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    for k in range(3):
                        if j == k:
                            continue
                        for pi in range(3):
                            if pi == i:
                                continue
                            for pj in range(3):
                                if pj == j:
                                    continue
                                for pk in range(3):
                                    if pk == k:
                                        continue
                                    dp[idx][i][j][k] += dp[idx - 1][pi][pj][pk]
                                    dp[idx][i][j][k] %= MOD

        ans = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ans += dp[n - 1][i][j][k]
        return ans % MOD
