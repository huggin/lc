class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count(n):
            ans = 0
            while n:
                ans += 1
                n &= n - 1
            return ans

        m = count(num2)
        ans = 0
        for i in range(31, -1, -1):
            if num1 & (1 << i) and m > 0:
                m -= 1
                ans ^= 1 << i
        for i in range(31):
            if (num1 & (1 << i)) == 0 and m > 0:
                m -= 1
                ans ^= 1 << i
        return ans
