class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 not in nums:
            return n - 1
        
        zero = 0
        j = 0
        ans = 0
        for i in range(n):
            while j < n and zero == 1 and nums[i] == 0:
                if nums[j] == 0:
                    zero = 0
                j += 1
            ans = max(ans, i - j)
            if nums[i] == 0:
                zero = 1
        return ans
