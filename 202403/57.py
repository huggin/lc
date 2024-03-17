class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        for a in intervals:
            if len(ans) == 0 or ans[-1][1] < a[0]:
                ans.append(a)
            else:
                ans[-1][1] = max(ans[-1][1], a[1])

        return ans
