class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        ans = 0
        for i in range(len(nums) - 1):
            l += nums[i]
            r -= nums[i]
            if l >= r:
                ans += 1
        return ans
