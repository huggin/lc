class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = sum(1 for c in s if c == "0")
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                if int(s[i:], 2) <= k:
                    ans += 1
                else:
                    break

        return ans
