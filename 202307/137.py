from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = [0] * 32
        for a in nums:
            for i in range(32):
                if a & (1 << i):
                    mask[i] += 1

        ans = 0
        for i in range(32):
            if mask[i] % 3 == 1:
                ans |= 1 << i

        if mask[31] % 3 == 1:
            return ans - (1 << 32)
        return ans
