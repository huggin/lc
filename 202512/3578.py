class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        presum = [0] * (n + 1)
        dp[0] = 1
        presum[0] = 1

        j = 0
        sl = SortedList()

        for i in range(n):
            sl.add(nums[i])
            while sl[-1] - sl[0] > k:
                idx = sl.bisect_left(nums[j])
                j += 1
                sl.pop(idx)

            dp[i + 1] = (presum[i] - presum[j - 1] + MOD) % MOD if j > 0 else presum[i]
            presum[i + 1] = (presum[i] + dp[i + 1]) % MOD

        return dp[n]
