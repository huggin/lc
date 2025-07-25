class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        for c in nums:
            if c > 0:
                s.add(c)

        if len(s) > 0:
            return sum(s)

        return max(nums)
