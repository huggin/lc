from sortedcontainers import SortedList


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        a = SortedList()
        ans = 24 * 60
        for t in timePoints:
            m, s = map(int, t.split(":"))
            t = m * 60 + s
            if len(a) == 0:
                a.add(t)
                continue
            i = bisect.bisect_left(a, t)
            if i == len(a):
                ans = min(ans, t - a[-1], a[0] + 24 * 60 - t)
            else:
                if a[i] == t:
                    return 0
                ans = min(ans, a[i] - t)
                if t > a[i - 1]:
                    ans = min(ans, t - a[i - 1])
                else:
                    ans = min(ans, t + 24 * 60 - a[i - 1])
            a.add(t)
        return ans
