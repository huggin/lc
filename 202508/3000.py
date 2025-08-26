class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mi = 0
        ans = 0
        for a, b in dimensions:
            d = a * a + b * b
            if mi < d or mi == d and a * b > ans:
                mi = d
                ans = a * b
        return ans
