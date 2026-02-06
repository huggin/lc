class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        j = 0
        ans = 0
        for i in range(n):
            while nums[j] * k < nums[i]:
                j += 1
            ans = max(ans, i - j + 1)
        return n - ans
