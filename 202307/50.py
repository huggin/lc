class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        flag = False
        if n < 0:
            n = -n
            flag = True
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return 1 / ans if flag else ans
