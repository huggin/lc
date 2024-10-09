class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif cnt == 0:
                ans += 1
            else:
                cnt -= 1
        return cnt + ans
