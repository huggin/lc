class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        n = len(nums)
        ans = [0] * n
        a = 0
        for c in nums:
            a ^= c
        ans[0] = a ^ mask

        for i in range(1, n):
            a ^= nums[n - i]
            ans[i] = mask ^ a
        return ans
