class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def ok(v):
            dp = [0] * n

            for i in range(n):
                if i == 0:
                    dp[0] = 1 if nums[0] <= v else 0
                elif i == 1:
                    dp[i] = 1 if nums[1] <= v or dp[0] == 1 else 0
                else:
                    dp[i] = dp[i - 1]
                    if nums[i] <= v:
                        dp[i] = max(dp[i], dp[i - 2] + 1)
            return dp[-1] >= k

        ans = 1
        lo, hi = 1, max(nums)
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
