class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]

        ans = -float("inf")
        dp = []
        for i in range(k):
            dp.append(presum[i])

        for i in range(k - 1, n):
            j = (i + 1) % k
            ans = max(ans, presum[i + 1] - dp[j])
            dp[j] = min(dp[j], presum[i + 1])

        return ans
