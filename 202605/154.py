class Solution:
    def findMin(self, nums: List[int]) -> int:
        def f(i, j):
            if i == j:
                return nums[i]
            if i + 1 == j:
                return min(nums[i], nums[j])
            k = i + j >> 1
            if nums[i] > nums[k]:
                return f(i, k)
            elif nums[k] > nums[j]:
                return f(k, j)
            return min(f(i, k), f(k, j))

        return f(0, len(nums) - 1)
