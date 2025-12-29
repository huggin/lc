class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j = -1
        for i, v in enumerate(nums):
            if v == 1:
                if j != -1:
                    if i - j <= k:
                        return False
                j = i
        return True
