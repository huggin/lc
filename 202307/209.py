from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, s = 0, 0
        ans = 1000000
        n = len(nums)
        for i in range(n):
            s += nums[i]
            if s >= target:
                while j <= i and s >= target:
                    ans = min(ans, i - j + 1)
                    s -= nums[j]
                    j += 1

        return 0 if ans == 1000000 else ans
