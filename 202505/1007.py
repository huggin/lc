class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = n

        def f(a, b):
            temp = 0
            for j in range(n):
                if a[j] == i:
                    continue
                elif b[j] == i:
                    temp += 1
                else:
                    temp = n
                    break
            return temp

        for i in range(1, 7):
            ans = min(ans, f(tops, bottoms), f(bottoms, tops))
        return ans if ans < n else -1
