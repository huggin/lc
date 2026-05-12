class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        ans = 0
        curr = 0
        for f, r in tasks:
            if curr <= r:
                ans += r - curr
                curr = r - f
            else:
                curr -= f
        return ans
