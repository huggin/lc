class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans = 1
        dir = 1
        while time > 0:
            ans += dir
            if ans == n:
                dir = -1
            if ans == 1:
                dir = 1
            time -= 1
        return ans
