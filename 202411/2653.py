class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def f(limit):
            ans = 0
            for i in range(n):
                j = bisect.bisect(nums, limit - nums[i])
                if j > i:
                    ans += j - i - 1
            return ans

        return f(upper) - f(lower - 1)
