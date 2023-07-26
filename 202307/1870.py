class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        lo, hi = 1, max(dist) * 100

        def ok(speed):
            ans = 0
            for i in range(n - 1):
                ans += math.ceil(dist[i] / speed)
            ans += dist[-1] / speed
            if ans <= hour:
                return True
            return False

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
