class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        curr = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            ans = max(curr, ans)
        curr = 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                curr += 1
            else:
                curr = 1
            ans = max(curr, ans)
        return ans
