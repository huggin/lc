class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        curr = -float("inf")
        for p in points:
            if p[0] > curr:
                curr = p[1]
                ans += 1

        return ans
