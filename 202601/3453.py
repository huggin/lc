class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        hi = 0
        lo = 10**9
        for x, y, l in squares:
            hi = max(hi, y + l)
            lo = min(lo, y)

        def ok(v):
            ans = 0
            for x, y, l in squares:
                if y + l <= v:
                    ans -= l * l
                elif y >= v:
                    ans += l * l
                else:
                    ans += ((y + l) - v) * l - (v - y) * l
            return ans

        while hi - lo > 1e-6:
            mi = (hi + lo) / 2
            v = ok(mi)
            if v > 0:
                lo = mi
            else:
                hi = mi
        return lo
