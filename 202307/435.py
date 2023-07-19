class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        prev = -int(1e6)
        ans = 0
        for a in intervals:
            if a[0] >= prev:
                ans += 1
                prev = a[1]

        return len(intervals) - ans
