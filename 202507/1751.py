class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        @cache
        def f2(j):
            i = j + 1
            while i < n and events[i][0] <= events[j][1]:
                i += 1
            return i

        @cache
        def f(j, k):
            if k == 0 or j == n:
                return 0

            ans = f(j + 1, k)
            i = f2(j)
            ans = max(ans, events[j][2] + f(i, k - 1))
            return ans

        return f(0, k)
