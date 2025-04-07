class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tt = sum(nums)
        if tt & 1:
            return False
        half = tt // 2
        dp = [0] * (half + 1)
        dp[0] = 1
        for a in nums:
            for i in range(half, -1, -1):
                if i - a >= 0 and dp[i - a]:
                    dp[i] = 1

        return dp[half] == 1
