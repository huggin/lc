class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for a in nums:
            if a in d:
                d[a * a] = d[a] + 1
            else:
                d[a * a] = 1

        ans = max(d.values())
        return ans if ans != 1 else -1
