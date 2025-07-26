class Solution:
    def maxSubarrays(self, n: int, pairs: List[List[int]]) -> int:
        m = len(pairs)
        pa = [[] for _ in range(n + 1)]
        for x, y in pairs:
            if x > y:
                x, y = y, x
            pa[x].append(y)

        ans = 0
        extra = [0] * (n + 2)
        b1, b2 = n + 1, n + 1
        for i in range(n, 0, -1):
            for b in pa[i]:
                if b < b1:
                    b1, b2 = b, b1
                elif b < b2:
                    b2 = b

            ans += b1 - i
            extra[b1] += b2 - b1

        return ans + max(extra)
