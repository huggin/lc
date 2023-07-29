class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0

        @cache
        def f(a, b):
            if a <= 0:
                if b > 0:
                    return 1
                else:
                    return 0.5
            if b <= 0:
                return 0

            ans = 0.25 * f(a - 100, b)
            ans += 0.25 * f(a - 75, b - 25)
            ans += 0.25 * f(a - 50, b - 50)
            ans += 0.25 * f(a - 25, b - 75)
            return ans

        return f(n, n)
