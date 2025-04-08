class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        j = 0
        for i in range(n - 1, -1, -1):
            if nums[i] in s:
                j = i + 1
                break
            s.add(nums[i])
        return (j + 2) // 3
