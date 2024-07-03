class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = nums[-1] - nums[3]
        ans = min(ans, nums[-2] - nums[2])
        ans = min(ans, nums[-3] - nums[1])
        ans = min(ans, nums[-4] - nums[0])
        return ans
