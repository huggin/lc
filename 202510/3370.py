class Solution:
    def smallestNumber(self, n: int) -> int:
        a = 1
        while (1 << a) - 1 < n:
            a += 1
        return (1 << a) - 1
