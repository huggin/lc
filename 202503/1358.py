class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        unique = 0
        n = len(s)
        cnt = [0] * 3
        l = 0
        for i in range(n):
            while l < n and unique < 3:
                cnt[ord(s[l]) - ord("a")] += 1
                if cnt[ord(s[l]) - ord("a")] == 1:
                    unique += 1
                l += 1
            if unique == 3:
                ans += n - l + 1
            cnt[ord(s[i]) - ord("a")] -= 1
            if cnt[ord(s[i]) - ord("a")] == 0:
                unique -= 1
        return ans
