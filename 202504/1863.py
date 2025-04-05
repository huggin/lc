class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1 << n):
            temp = 0
            for j in range(n):
                if i & (1 << j):
                    temp ^= nums[j]
            ans += temp
        return ans
