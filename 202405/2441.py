class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for a in nums:
            if a > 0 and -a in s:
                ans = max(ans, a)
        return ans
