class Solution:
    def findComplement(self, num: int) -> int:
        a = 1
        while a <= num:
            a *= 2
        return a - num - 1
