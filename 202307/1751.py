class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        @cache
        def f(j, k):
            if k == 0:
                return 0
            if j == n:
                return 0

            ans = f(j + 1, k)
            i = j + 1
            while i < n and events[i][0] <= events[j][1]:
                i += 1
            ans = max(ans, events[j][2] + f(i, k - 1))
            return ans

        return f(0, k)
