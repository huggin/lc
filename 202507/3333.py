class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = int(1e9 + 7)
        a = []
        for i, c in enumerate(word):
            if i == 0 or word[i] != word[i - 1]:
                a.append(1)
            else:
                a[-1] += 1

        m = len(a)
        ans = 1
        for i in range(m):
            ans = (ans * a[i]) % MOD
        if m >= k:
            return ans

        k -= m + 1
        b = [c - 1 for c in a if c > 1]
        m = len(b)

        dp = [0] * (k + 1)
        dp[0] = 1
        for c in b:
            dp2 = [0] * (k + 1)
            total = 0
            for i in range(k + 1):
                total = (total + dp[i]) % MOD
                if i > c:
                    total = (total + MOD - dp[i - c - 1]) % MOD
                dp2[i] = total
            dp = dp2

        return (ans - sum(dp) + MOD) % MOD
