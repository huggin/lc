class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def ok(v):
            cnt = 0
            for c in candies:
                cnt += c // v
            return cnt >= k

        ans = 0
        lo, hi = 1, max(candies)
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return ans
