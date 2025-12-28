class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        mi = nums[0] - k
        for i in range(1, len(nums)):
            if nums[i] + k > mi:
                ans += 1
                mi = max(mi + 1, nums[i] - k)
        return ans
