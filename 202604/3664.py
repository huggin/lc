class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        a = []
        for x, y in points:
            if x == 0:
                a.append(y)
            elif y == side:
                a.append(side + x)
            elif x == side:
                a.append(side * 2 + side - y)
            else:
                a.append(side * 3 + side - x)
        
        n = len(points)
        a.sort()
        a = a + list(c + 4 * side for c in a)
        
        def ok(v):
            for i in range(n):
                cnt = 1
                curr = a[i]
                while cnt < k:
                    j = bisect_left(a, curr + v)
                    if j == len(a):
                        break
                    cnt += 1
                    curr = a[j]
                if cnt == k and a[i+n] - a[j] >= v:
                    return True
            return False

        ans = 1
        lo, hi = 1, side
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return ans
