class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        a = [0] * (max(fruits[-1][0], startPos) + 1)
        for i, v in fruits:
            a[i] = v

        ps = [0]
        for c in a:
            ps.append(ps[-1] + c)

        ans = 0

        for i in range(0, k // 2 + 1):
            s = startPos - (k - i * 2)
            if s < 0:
                s = 0
            e = startPos + i
            if e >= len(ps) - 1:
                e = len(ps) - 2
            ans = max(ans, ps[e + 1] - ps[s])

        for i in range(0, k // 2 + 1):
            s = startPos - i
            if s < 0:
                s = 0
            e = startPos + (k - i * 2)
            if e >= len(ps) - 1:
                e = len(ps) - 2
            ans = max(ans, ps[e + 1] - ps[s])
        return ans
