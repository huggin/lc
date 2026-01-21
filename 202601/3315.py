class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            if nums[i] == 2:
                ans[i] == -1
            else:
                for j in range(32):
                    if (nums[i] & (1 << j)) == 0:
                        k = j
                        break
                ans[i] = nums[i] & ~(1 << k - 1)
        return ans
