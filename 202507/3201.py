class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(2)]
        for a in nums:
            if a & 1:
                dp[1][0] = dp[1][0] + 1
                dp[1][1] = dp[0][1] + 1
            else:
                dp[0][0] = dp[0][0] + 1
                dp[0][1] = dp[1][1] + 1

        return max(max(row) for row in dp)
