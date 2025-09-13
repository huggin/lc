class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        v, c = 0, 0
        for i in ["a", "e", "i", "o", "u"]:
            v = max(v, cnt[ord(i) - ord("a")])
        for i in range(26):
            if chr(ord("a") + i) not in ["a", "e", "i", "o", "u"]:
                c = max(c, cnt[i])
        return v + c
