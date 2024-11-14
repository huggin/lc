class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        ans = -1

        def ok(v):
            cnt = 0
            for q in quantities:
                cnt += (q + v - 1) // v
            return cnt <= n

        lo, hi = 1, max(quantities)
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
