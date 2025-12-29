class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
        if gcd(*nums) != 1:
            return -1
        n = len(nums)
        a = []
        dp = [[0] * n for _ in range(n)]
        dp[0] = nums
        mi = -1
        for i in range(1, n):
            for j in range(n - i):
                dp[i][j] = gcd(dp[i - 1][j], dp[i - 1][j + 1])
            if 1 in dp[i]:
                mi = i + 1
                break
        return mi + n - 2
