class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * 1024
        cnt[0] = 1
        curr = 0
        ans = 0
        for c in word:
            curr ^= 1 << ord(c) - ord("a")
            ans += cnt[curr]
            for i in range(10):
                ans += cnt[curr ^ (1 << i)]
            cnt[curr] += 1

        return ans
