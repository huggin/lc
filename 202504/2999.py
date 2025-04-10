class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        finish = list(int(c) for c in str(finish))
        start = list(int(c) for c in str(start - 1))
        m = len(s)
        if len(finish) < m:
            return 0

        s1 = "".join(str(c) for c in finish[-m:])
        s2 = "".join(str(c) for c in start[-m:]) if len(start) >= m else None

        def f(a, ss):
            if ss is None:
                return 0
            n = len(a)

            @cache
            def g(i, j):
                if n - i == m:
                    if j == 0 or ss >= s:
                        return 1
                    return 0
                ma = min(limit, a[i]) if j == 1 else limit
                ans = 0
                for k in range(ma + 1):
                    nj = 1 if j == 1 and k == a[i] else 0
                    ans += g(i + 1, nj)
                return ans

            return g(0, 1)

        return f(finish, s1) - f(start, s2)
