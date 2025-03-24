class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = meetings[0][0] - 1
        curr = meetings[0][1]
        for i in range(1, len(meetings)):
            if meetings[i][0] - curr > 0:
                ans += meetings[i][0] - curr - 1
                curr = meetings[i][1]
            else:
                curr = max(curr, meetings[i][1])
        return ans + days - curr
