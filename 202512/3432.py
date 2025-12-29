class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            if (sum(nums[0 : i + 1]) - sum(nums[i + 1 :])) % 2 == 0:
                ans += 1
        return ans
