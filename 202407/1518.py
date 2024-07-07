class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        ans = 0
        e = 0
        while b > 0:
            ans += b
            e += b
            b = e // n
            e = e % n
        return ans
