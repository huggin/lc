class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def ok(v):
            curr = position[0]
            cnt = 1
            for i in range(1, n):
                if position[i] - curr >= v:
                    cnt += 1
                    curr = position[i]
            return cnt >= m

        ans = -1
        lo, hi = 0, position[-1]
        while lo <= hi:
            mi = (lo + hi) >> 1
            if ok(mi):
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return ans
