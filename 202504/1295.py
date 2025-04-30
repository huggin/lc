class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 if len(str(c)) % 2 == 0 else 0 for c in nums)
