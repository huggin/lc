class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        ans = 0
        n = len(bottomLeft)
        for i in range(n):
            x1, y1 = bottomLeft[i][0], bottomLeft[i][1]
            x2, y2 = topRight[i][0], topRight[i][1]
            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j][0], bottomLeft[j][1]
                x4, y4 = topRight[j][0], topRight[j][1]
                if x1 >= x4 or y1 >= y4 or x3 >= x2 or y3 >= y2:
                    continue
                length = min(min(x2, x4) - max(x1, x3), min(y2, y4) - max(y1, y3))
                ans = max(ans, length**2)
        return ans
