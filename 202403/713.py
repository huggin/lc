class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        curr = 1
        j = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            curr *= nums[i]
            while j <= i and curr >= k:
                curr //= nums[j]
                j += 1
            ans += i - j + 1
        return ans
