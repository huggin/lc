class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {}
        idx[0] = -1
        mask = 0
        b = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        ans = 0
        for k, c in enumerate(s):
            if c in b:
                mask ^= 1 << b[c]

            if mask in idx:
                ans = max(ans, k - idx[mask])
            else:
                idx[mask] = k
        return ans
