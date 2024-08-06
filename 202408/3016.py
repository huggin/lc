class Solution:
    def minimumPushes(self, word: str) -> int:
        j = 0
        ans = 0
        for k, v in Counter(word).most_common():
            if j >= 24:
                ans += v * 4
            elif j >= 16:
                ans += v * 3
            elif j >= 8:
                ans += v * 2
            else:
                ans += v
            j += 1
        return ans
