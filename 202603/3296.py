class Solution:
    def minNumberOfSeconds(self, h: int, w: List[int]) -> int:
        def ok(v):
            cnt = 0
            for a in w:
                k = math.isqrt(v * 2 // a)
                while k * (k + 1) // 2 * a <= v:
                    k += 1
                cnt += k - 1
            return cnt >= h

        ans = -1
        lo, hi = 1, 10**17
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1

        return ans
