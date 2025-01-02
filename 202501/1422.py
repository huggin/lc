class Solution:
    def maxScore(self, s: str) -> int:
        return max(
            sum(1 if c == "0" else 0 for c in s[0:i])
            + sum(1 if c == "1" else 0 for c in s[i : len(s)])
            for i in range(1, len(s))
        )
