class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        MOD = 10**9 + 7
        for i in range(n):
            j = bisect.bisect(nums, target - nums[i], lo=i)
            if j > i:
                ans += pow(2, j - i - 1, MOD)
                if ans >= MOD:
                    ans -= MOD
        return ans % MOD
