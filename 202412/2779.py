class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 1
        for i in range(n):
            j = bisect.bisect(nums, nums[i] + k + k, lo=i + 1)
            ans = max(ans, j - i)
        return ans
