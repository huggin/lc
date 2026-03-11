class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        a = 1
        while a <= n:
            a <<= 1
        return a - n - 1
