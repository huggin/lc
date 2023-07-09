class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]

        def f(c, d, s):
            cnt1, cnt2 = 0, 0
            ans = 0
            for i in range(n):
                if s[i] == c:
                    cnt1 += 1
                elif s[i] == d:
                    cnt2 += 1
                else:
                    continue
                if cnt1 < cnt2:
                    cnt1, cnt2 = 0, 0
                if cnt1 > 0 and cnt2 > 0:
                    ans = max(ans, cnt1 - cnt2)

            return ans

        ans = 0
        a = set(s)
        for c in a:
            for d in a:
                if c == d:
                    continue
                ans = max(ans, f(c, d, s))
                ans = max(ans, f(c, d, s2))

        return ans
