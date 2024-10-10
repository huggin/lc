class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        n = len(nums)
        for i in range(n):
            if len(s) == 0 or nums[s[-1]] > nums[i]:
                s.append(i)

        ans = 0
        for j in range(n - 1, -1, -1):
            while len(s) > 0 and nums[j] >= nums[s[-1]]:
                ans = max(ans, j - s[-1])
                s.pop()

        return ans
