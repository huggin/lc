class Solution:
    def strangePrinter(self, s: str) -> int:
        a = []
        for c in s:
            if len(a) == 0 or a[-1] != c:
                a.append(c)
        n = len(a)

        @cache
        def f(i, j, curr="$"):
            if i > j:
                return 0
            if a[i] == curr:
                return f(i + 1, j, curr)
            if a[j] == curr:
                return f(i, j - 1, curr)

            if a[i] == a[j]:
                return f(i + 1, j - 1, a[i]) + 1

            ans = min(f(i + 1, j, a[i]), f(i, j - 1, a[j])) + 1
            for k in range(i, j + 1):
                if a[k] == curr:
                    ans = min(ans, f(i + 1, k - 1, a[i]) + f(k + 1, j, curr) + 1)
                    ans = min(ans, f(i, k - 1, curr) + f(k + 1, j - 1, a[j]) + 1)

            return ans

        return f(0, n - 1)
