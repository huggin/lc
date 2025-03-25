class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x, y = [], []
        for x1, y1, x2, y2 in rectangles:
            x.append((x1, 1))
            x.append((x2, -1))
            y.append((y1, 1))
            y.append((y2, -1))

        x.sort()
        y.sort()

        def f(a):
            cnt = 0
            ans = 0
            for i in range(len(a)):
                cnt += a[i][1]
                if cnt == 0:
                    ans += 1
                if ans > 2:
                    return True
            return False

        return f(x) or f(y)
