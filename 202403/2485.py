class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = sum(range(1, n + 1))
        s = 0
        for i in range(1, n + 1):
            s += i
            if tot - s + i == s:
                return i
        return -1
