class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0
        j = 0
        diff = [0] * n
        for i in range(n):
            diff[i] = abs(ord(s[i]) - ord(t[i])) 
        for i in range(n):
            maxCost -= diff[i]
            while maxCost < 0:
                maxCost += diff[j]
                j += 1
            ans = max(ans, i - j + 1)
        return ans
