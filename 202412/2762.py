from sortedcontainers import SortedList


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        s = SortedList()
        j = 0
        ans = 0
        for a in nums:
            s.add(a)
            while s[-1] - s[0] > 2:
                s.pop(s.bisect_left(nums[j]))
                j += 1
            ans += len(s)
        return ans
