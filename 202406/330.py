class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        curr = 0
        i = 0
        while curr < n and i < len(nums):
            if nums[i] <= curr + 1:
                curr += nums[i]
                i += 1
            else:
                curr += curr + 1
                ans += 1
        while curr < n:
            curr += curr + 1
            ans += 1
            
        return ans
