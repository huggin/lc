class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 0
        for i in range(k):
            if s[i] in ["a", "e", "i", "o", "u"]:
                v += 1

        ans = v
        n = len(s)
        for i in range(k, n):
            if s[i] in ["a", "e", "i", "o", "u"]:
                v += 1
            if s[i - k] in ["a", "e", "i", "o", "u"]:
                v -= 1
            ans = max(ans, v)

        return ans
