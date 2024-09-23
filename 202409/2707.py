class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic = set(dictionary)
        n = len(s)

        @cache
        def f(k):
            if k == n:
                return 0
            ans = 1 + f(k + 1)
            for i in range(k, n):
                if s[k : i + 1] in dic:
                    ans = min(ans, f(i + 1))
            return ans

        return f(0)
