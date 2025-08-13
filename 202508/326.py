class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n:
            if n % 3 == 2:
                return False
            if n % 3 == 1 and n != 1:
                return False
            n //= 3
        return True
