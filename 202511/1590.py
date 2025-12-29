class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        s %= p
        if s == 0:
            return 0

        d = {}
        d[0] = -1
        curr = 0
        ans = len(nums)
        for i, v in enumerate(nums):
            curr = (curr + v) % p
            if (curr - s + p) % p in d:
                ans = min(ans, i - d[(curr - s + p) % p])
            d[curr] = i

        return ans if ans != len(nums) else -1
