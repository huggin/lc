class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, 1 << n):
            curr = 0
            for j in range(n):
                if i & (1 << j):
                    curr ^= nums[j]
            ans += curr
        return ans
