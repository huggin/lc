class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        s = int(s, 2)
        while s != 1:
            if s & 1:
                s += 1
            else:
                s //= 2
            ans += 1
        return ans
