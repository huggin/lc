class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        p = 31
        m = int(1e9 + 9)
        n = len(s)
        p_pow = [0] * (n)
        p_pow[0] = 1
        for i in range(1, n):
            p_pow[i] = p_pow[i - 1] * p % m

        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + (ord(s[i]) - ord("a") + 1) * p_pow[i]) % m

        r = 0
        for i in range(n - 1, -1, -1):
            r = (r + (ord(s[i]) - ord("a") + 1) * p_pow[n - 1 - i]) % m

        if r == h[n]:
            return s

        for i in range(n - 1, -1, -1):
            r = (r + m - (ord(s[i]) - ord("a") + 1) * p_pow[n - 1 - i] % m) % m
            if r == h[i] * p_pow[n - i] % m:
                t = s[i:]
                return t[::-1] + s

        return ""
