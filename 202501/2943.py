class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def f(a, n):
            a.sort()
            ans = 2
            curr = 1
            for i in range(1, len(a)):
                if a[i] == a[i - 1] + 1:
                    curr += 1
                else:
                    ans = max(ans, curr + 1)
                    curr = 1
            ans = max(ans, curr + 1)
            return ans

        return min(f(hBars, n), f(vBars, m)) ** 2
