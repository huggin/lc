class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for k, v in enumerate(nums):
            if v <= 0:
                nums[k] = n + 1
        
        for i in range(n):
            if abs(nums[i]) <= n and nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        
        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1
