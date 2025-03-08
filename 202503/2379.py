class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a = [1 if c == "B" else 0 for c in blocks]
        n = len(a)
        ans = k
        for i in range(n - k + 1):
            ans = min(ans, k - sum(a[i : i + k]))
        return ans
