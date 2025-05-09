class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        a = list(int(c) for c in num)
        tt = sum(a)
        if tt & 1:
            return 0

        freq = [0] * 10
        for c in a:
            freq[c] += 1
        n = len(a)
        fa = [1] * (n + 1)
        for i in range(1, n + 1):
            fa[i] = fa[i - 1] * i % MOD

        fact = 1
        for i in range(10):
            fact = fact * fa[freq[i]] % MOD

        half = tt // 2
        m = n // 2

        dp = [[[-1] * (half + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        def f(i, e, curr):
            if e > m or curr > half:
                return 0
            if i == n:
                if e == m and curr == half:
                    return 1
                return 0
            if dp[i][e][curr] != -1:
                return dp[i][e][curr]
            dp[i][e][curr] = (f(i + 1, e, curr) + f(i + 1, e + 1, curr + a[i])) % MOD
            return dp[i][e][curr]

        ans = f(0, 0, 0) * fa[m] % MOD * fa[n - m] % MOD

        return ans * pow(fact, MOD - 2, MOD) % MOD
