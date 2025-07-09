class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        tot = 0
        n = len(startTime)
        for i in range(k):
            tot += endTime[i] - startTime[i]

        end = eventTime if k == n else startTime[k]
        ans = end - tot
        for i in range(k, n):
            tot -= endTime[i - k] - startTime[i - k]
            tot += endTime[i] - startTime[i]
            end = eventTime if i == n - 1 else startTime[i + 1]
            start = endTime[i - k]
            ans = max(ans, end - start - tot)
        return ans
