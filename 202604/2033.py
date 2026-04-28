class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = []
        for row in grid:
            for item in row:
                a.append(item)
        a.sort()
        mid = a[len(a) // 2]
        ans = 0
        for v in a:
            if (v - mid) % x != 0:
                return -1
            ans += abs(v - mid) // x
        return ans
