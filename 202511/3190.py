class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for a in nums if a % 3)
