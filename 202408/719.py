class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1]
        ans = -1
        n = len(nums)
        tot = n * (n - 1) // 2

        def ok(v):
            ans = 0
            for a in nums:
                j = bisect.bisect_right(nums, a + v)
                ans += n - j
            return tot - ans >= k

        while lo <= hi:
            mi = (lo + hi) >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1

        return ans
