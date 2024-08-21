class Solution:
    def strangePrinter(self, s: str) -> int:
        a = []
        for c in s:
            if len(a) == 0 or a[-1] != c:
                a.append(c)

        @cache
        def f(i, j):
            if i == j:
                return 1
            if a[i] == a[j]:
                return f(i, j - 1)
            ans = 100
            for k in range(i, j):
                ans = min(ans, f(i, k) + f(k + 1, j))
            return ans

        return f(0, len(a) - 1)
