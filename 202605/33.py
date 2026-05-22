class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = lo + hi >> 1
            if nums[mi] == target:
                return mi
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            elif nums[lo] < nums[mi]:
                if nums[lo] < target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                if nums[mi] < target < nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
        return -1
