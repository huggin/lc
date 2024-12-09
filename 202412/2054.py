from sortedcontainers import SortedList


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[1], x[0]))
        a = SortedList()
        ans = 0
        for s, e, v in events:
            idx = a.bisect_left((s, 0))
            if idx > 0:
                ans = max(ans, v + a[idx - 1][1])
            else:
                ans = max(ans, v)
            idx = a.bisect_left((e + 1, 0))
            if idx > 0:
                v = max(v, a[idx - 1][1])
            a.add((e, v))
        return ans
