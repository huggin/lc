class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = sorted(nums[1:])
        return nums[0] + a[0] + a[1]
