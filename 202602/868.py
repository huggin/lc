class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        ans = 0
        j = -1
        for i in range(len(s)):
            if s[i] == "1":
                if j != -1:
                    ans = max(ans, i - j)
                j = i
        return ans
