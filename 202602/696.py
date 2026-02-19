class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        cnt1, cnt2 = 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(cnt1, cnt2)
                cnt1 = cnt2
                cnt2 = 1
            else:
                cnt2 += 1
            
        return ans + min(cnt1, cnt2)
