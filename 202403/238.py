class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = reduce(lambda x, y: x * y, nums)
        zero = sum(1 for c in nums if c == 0)
        if zero >= 2:
            return [0] * len(nums)
        if zero == 0:
            return [s // c for c in nums]
        s = 1
        for a in nums:
            if a != 0:
                s *= a

        return [0 if a != 0 else s for a in nums]
