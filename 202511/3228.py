class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        n = len(s)
        cnt = 0
        zero = True
        for i in range(n):
            if s[i] == "1":
                cnt += 1
                zero = False
            elif not zero:
                ans += cnt
                zero = True
        return ans
