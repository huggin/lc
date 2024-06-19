class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        lo, hi = 1, max(bloomDay)
        ans = -1

        def ok(v):
            cnt = 0
            j = 0
            tot = 0
            while j < n:
                if bloomDay[j] <= v:
                    cnt += 1
                    if cnt == k:
                        tot += 1
                        cnt = 0
                else:
                    cnt = 0
                j += 1
            return tot >= m

        while lo <= hi:
            mi = (lo + hi) >> 1
            if ok(mi):
                hi = mi - 1
                ans = mi
            else:
                lo = mi + 1
        return ans
