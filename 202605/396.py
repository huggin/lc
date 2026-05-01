class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += nums[i] * i
        tt = sum(nums)
        curr = ans
        for i in range(1, n):
            curr = curr - nums[n-i] * (n - 1) + (tt - nums[n-i])
            ans = max(ans, curr)
        return ans
