class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        prev = -1
        for i in range(n):
            if prev == -1 or nums[i] > prev + k:
                ans += 1
                prev = nums[i]
        return ans
