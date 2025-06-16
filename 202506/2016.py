class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[j] - nums[i]
                if d > 0:
                    ans = max(ans, d)
        return ans
