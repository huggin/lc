class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        n = len(nums)
        d1 = {}
        d2 = {}

        for i in range(n):
            if nums[i] not in d1:
                d1[nums[i]] = i
            elif nums[i] not in d2:
                d2[nums[i]] = d1[nums[i]]
                d1[nums[i]] = i
            else:
                ans = min(ans, 2 * (i - d2[nums[i]]))
                d2[nums[i]] = d1[nums[i]]
                d1[nums[i]] = i

        return -1 if ans == float("inf") else ans
