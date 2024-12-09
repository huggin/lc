class Solution:
    def minimumSize(self, nums: List[int], m: int) -> int:
        def ok(v):
            cnt = 0
            for a in nums:
                cnt += (a - 1) // v
            return cnt <= m

        lo, hi = 1, max(nums)

        ans = 1
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1

        return ans
