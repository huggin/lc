class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contain(k):
            while k > 0:
                if k % 10 == 0:
                    return False
                k //= 10
            return True

        for i in range(1, n):
            if contain(i) and contain(n - i):
                return [i, n - i]
        return [-1, -1]
