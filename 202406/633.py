class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()
        i = 0
        d = i * i
        while d <= c:
            if c - d in s or d + d == c:
                return True
            s.add(d)
            i += 1
            d = i * i
        return False
