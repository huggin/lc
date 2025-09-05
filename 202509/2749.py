class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 > 0 and ans <= 60:
            num1 -= num2
            ans += 1
            if num1 > 0 and num1 >= ans and num1.bit_count() <= ans:
                return ans
        return -1
