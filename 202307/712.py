from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        ps1 = [0] * n
        ps1[0] = ord(s1[0])
        for i in range(1, n):
            ps1[i] = ps1[i - 1] + ord(s1[i])

        m = len(s2)
        ps2 = [0] * m
        ps2[0] = ord(s2[0])
        for i in range(1, m):
            ps2[i] = ps2[i - 1] + ord(s2[i])

        @cache
        def f(i, j) -> int:
            if i < 0:
                if j < 0:
                    return 0
                return ps2[j]
            if j < 0:
                return ps1[i]
            if s1[i] == s2[j]:
                return f(i - 1, j - 1)

            return min(ord(s1[i]) + f(i - 1, j), ord(s2[j]) + f(i, j - 1))

        return f(n - 1, m - 1)
