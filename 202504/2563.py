class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for k in range(len(nums)):
            i = bisect_left(nums, lower - nums[k], hi=k)
            j = bisect_right(nums, upper - nums[k], hi=k)
            ans += j - i
        return ans
