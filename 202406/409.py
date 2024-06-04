class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = [0] * 52
        for c in s:
            if "a" <= c <= "z":
                cnt[ord(c) - ord("a")] += 1
            else:
                cnt[ord(c) - ord("A") + 26] += 1

        ans = 0
        for i in range(52):
            if cnt[i] % 2 == 0:
                ans += cnt[i]
            else:
                ans += cnt[i] - 1

        return ans if ans == len(s) else ans + 1
