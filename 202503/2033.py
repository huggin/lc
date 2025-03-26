class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = [c for row in grid for c in row]
        a.sort()
        n = len(a)
        for i in range(1, n):
            if (a[i] - a[i - 1]) % x != 0:
                return -1
        ave = a[n // 2]
        if (ave - a[0]) // x == 0:
            return sum(abs(c - ave) // x for c in a)

        ave1 = ((ave - a[0]) // x + 1) * x + a[0]
        ave2 = ((ave - a[0]) // x) * x + a[0]
        return min(
            sum(abs(c - ave1) // x for c in a), sum(abs(c - ave2) // x for c in a)
        )
