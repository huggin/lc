class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, n = 0, 0
        for a in nums:
            if a < 0:
                p += 1
            elif a > 0:
                n += 1
        return max(p, n)
