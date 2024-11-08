class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        a = set()
        n = len(s)

        self.ans = 0

        def f(k):
            if k == n:
                self.ans = max(self.ans, len(a))
                return

            for i in range(k, n):
                if s[k : i + 1] not in a:
                    a.add(s[k : i + 1])
                    f(i + 1)
                    a.remove(s[k : i + 1])

        f(0)
        return self.ans
