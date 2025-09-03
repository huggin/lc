class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        print(points)
        n = len(points)
        ans = 0
        for i in range(n):
            my = -float("inf")
            for j in range(i + 1, n):
                if points[j][1] <= points[i][1] and points[j][1] > my:
                    ans += 1
                    my = points[j][1]

        return ans
