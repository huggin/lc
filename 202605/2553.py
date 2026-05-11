class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(int(a) for a in "".join(str(c) for c in nums))
