class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def f(a):
            s = str(a * a)
            n = len(s)

            def dfs(k, curr):
                if curr > a:
                    return False
                if k == n:
                    if curr == a:
                        return True
                    return False
                ans = False
                for i in range(k, n):
                    if int(s[k : i + 1]) + curr <= a:
                        ans = ans or dfs(i + 1, int(s[k : i + 1]) + curr)
                return ans

            return dfs(0, 0)

        ans = 0
        for i in range(1, n + 1):
            if f(i):
                ans += i * i

        return ans
