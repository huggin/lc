class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        ans = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == ma:
                j = i
                while j < n and nums[j] == ma:
                    j += 1
                ans = max(ans, j - i)
                i = j
            else:
                i += 1
        return ans
