class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        j = -1
        for i in range(len(s)):
            if s[i] == "1":
                if j == -1:
                    j = i
                ans += i - j + 1
                if ans >= MOD:
                    ans -= MOD
            else:
                j = -1
        return ans
