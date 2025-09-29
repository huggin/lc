class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def f(i, j):
            if i + 2 > j:
                return 0
            ans = float("inf")
            for k in range(i + 1, j):
                temp = values[i] * values[k] * values[j] + f(i, k) + f(k, j)
                ans = min(temp, ans)
            return ans

        return f(0, len(values) - 1)
