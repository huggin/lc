class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        def f(c):
            ans = 0
            for i in range(len(s)):
                if c != s[i]:
                    ans += 1
                c = "1" if c == "0" else "0"
            return ans

        def f2(c1, c2):
            left = [0] * n
            right = [0] * n
            if s[0] != c1:
                left[0] = 1
            c1 = "1" if c1 == "0" else "0"
            for i in range(1, n):
                left[i] = left[i - 1]
                if c1 != s[i]:
                    left[i] += 1
                c1 = "1" if c1 == "0" else "0"
            if s[-1] != c2:
                right[-1] = 1
            c2 = "1" if c2 == "0" else "0"
            for i in range(n - 2, -1, -1):
                right[i] = right[i + 1]
                if c2 != s[i]:
                    right[i] += 1
                c2 = "1" if c2 == "0" else "0"
            ans = inf
            for i in range(0, n - 1):
                ans = min(ans, left[i] + right[i + 1])
            return ans

        if n % 2 == 0:
            return min(f("0"), f("1"))

        return min(f("0"), f("1"), f2("0", "1"), f2("1", "0"))
