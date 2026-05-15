class Solution:
    def findMin(self, nums: List[int]) -> int:
        def f(lo, hi):
            if lo == hi:
                return nums[lo]
            if lo + 1 == hi:
                return min(nums[lo], nums[hi])
            if nums[lo] < nums[hi]:
                return nums[lo]
            mi = lo + hi >> 1
            if nums[lo] < nums[mi]:
                return f(mi + 1, hi)
            else:
                return f(lo, mi)

        return f(0, len(nums) - 1)
