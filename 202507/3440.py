class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        s = [0] + startTime + [eventTime]
        e = [0] + endTime + [eventTime]
        n = len(s)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], s[i] - e[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], s[i + 1] - e[i])

        ans = 0
        for i in range(1, n - 1):
            need = e[i] - s[i]
            ans = max(ans, s[i + 1] - e[i - 1] - need)
            if need <= left[i - 1] or need <= right[i + 1]:
                ans = max(ans, s[i + 1] - e[i - 1])
        return ans
