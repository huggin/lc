class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = [0] * 26
        v = set()
        ans = [0] * 26
        for c in s:
            ans[ord(c) - ord("a")] = cnt[ord(c) - ord("a")].bit_count()
            for u in v:
                cnt[ord(u) - ord("a")] |= 1 << ord(c) - ord("a")
            v.add(c)
        return sum(ans)
