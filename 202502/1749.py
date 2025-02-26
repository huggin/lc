class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def f(b):
            ans = 0
            curr = 0
            for a in b:
                if curr + a > 0:
                    curr += a
                else:
                    curr = 0
                ans = max(curr, ans)
            return ans

        ans = f(nums)
        nums = [-a for a in nums]
        return max(ans, f(nums))
