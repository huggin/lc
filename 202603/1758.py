class Solution:
    def minOperations(self, s: str) -> int:
        def f(c):
            ans = 0
            for i in range(len(s)):
                if c != s[i]:
                    ans += 1
                c = "1" if c == "0" else "0"
            return ans

        return min(f("1"), f("0"))
