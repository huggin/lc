class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return (
                abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
                / 2
            )

        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, area(points[i], points[j], points[k]))
        return ans
