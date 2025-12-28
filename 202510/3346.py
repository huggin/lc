class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        C = Counter(nums)
        n = len(nums)
        ans = 0
        i, j = 0, 0
        for v in range(nums[0], nums[-1] + 1):
            while i < n and nums[i] - k <= v:
                i += 1
            while j < n and nums[j] + k < v:
                j += 1
            if i - j - C[v] > numOperations:
                ans = max(ans, C[v] + numOperations)
            else:
                ans = max(ans, i - j)
        return ans
