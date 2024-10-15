class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        cnt = 0
        ans = 0
        for c in s:
            if c == '0':
                ans += cnt
            else:
                cnt += 1
        return ans
