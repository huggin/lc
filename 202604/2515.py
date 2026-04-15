class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n
        for i, w in enumerate(words):
            if w == target:
                ans = min(
                    ans,
                    abs(i - startIndex),
                    abs(startIndex + n - i),
                    abs(startIndex - i),
                    abs(i + n - startIndex),
                )
        return -1 if ans == n else ans
