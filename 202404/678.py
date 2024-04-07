class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def f(i, j):
            if i > j or j == i and s[i] == "*":
                return True

            if s[i] == ")" or s[j] == "(":
                return False

            ans = f(i + 1, j - 1)
            if s[i] == "*":
                ans |= f(i + 1, j)
            if s[j] == "*":
                ans |= f(i, j - 1)

            for k in range(i, j):
                ans |= f(i, k) and f(k + 1, j)
            return ans

        return f(0, len(s) - 1)
