class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        return sum(1 if x != y else 0 for x, y in zip(a, heights))
