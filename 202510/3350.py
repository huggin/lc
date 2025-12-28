class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = [-1] * n
        left[0] = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                left[i] = left[i-1]
            else:
                left[i] = i
        
        right = [-1] * n
        right[n-1] = n-1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                right[i] = right[i+1]
            else:
                right[i] = i
        
        ans = 1
        for i in range(n-1):
            ans = max(ans, min(i-left[i]+1, right[i+1] - i))
        return ans
