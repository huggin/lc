class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        lo, hi = 0, sum(batteries) // n

        def ok(m):
            k = 0
            pre = 0
            for b in batteries:
                pre += b
                if pre >= m:
                    k += 1
                    pre -= m

            return k >= n

        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
