class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        ans = 0
        n = len(nums)
        curr = 0
        for i in range(n):
            if nums[i] == ma:
                curr += 1
            else:
                ans = max(curr, ans)
                curr = 0
        return max(ans, curr)
