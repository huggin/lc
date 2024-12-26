class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def f(k, curr):
            if k == n:
                if curr == target:
                    return 1
                return 0
            return f(k+1, curr+nums[k]) + f(k+1, curr-nums[k])
        
        return f(0, 0)
