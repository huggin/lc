class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = [Counter(w) for w in words]
        n = len(words)
        ans = []
        for k, v in s[0].items():
            for i in range(1, n):
                v = min(v, s[i][k])
            if v > 0:
                ans += [k] * v
        return ans
