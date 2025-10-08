class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        ans = [0] * len(spells)
        n = len(potions)
        for i, s in enumerate(spells):
            ans[i] = n - bisect.bisect_left(potions, (success + s - 1) // s)
        return ans
