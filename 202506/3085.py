class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        a = sorted(c.values())
        ans = float("inf")
        for i in a:
            temp = 0
            for j in a:
                if j < i:
                    temp += j
                elif i + k < j:
                    temp += j - i - k
            ans = min(ans, temp)
        return ans
