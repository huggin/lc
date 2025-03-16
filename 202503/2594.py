class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def ok(v):
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(v // r))
            return cnt >= cars

        lo, hi = 0, 10**15
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
