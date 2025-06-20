class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return ans
        for i in range(0, n, 3):
            ans.append(nums[i : i + 3])
        return ans
