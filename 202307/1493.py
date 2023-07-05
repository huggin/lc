from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        cnt = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
                while j < n and cnt > 1:
                    if nums[j] == 0:
                        cnt -= 1
                    j += 1

            ans = max(ans, i - j)

        return ans
