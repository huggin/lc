class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        t = 0
        for c in s:
            if c == "(":
                t += 1
                ans = max(t, ans)
            elif c == ")":
                t -= 1

        return ans
