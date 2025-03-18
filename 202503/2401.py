class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        mask = 0
        ans = 0
        for i in range(n):
            while mask & nums[i] != 0 and j < i:
                mask &= ~nums[j]
                j += 1
            mask |= nums[i]
            ans = max(ans, i - j + 1)
        return ans
