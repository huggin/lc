class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        dt = defaultdict(dict)
        dm = defaultdict(dict)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    a, b = 1, 0
                elif dy == 0:
                    a, b = 0, 1
                else:
                    g = gcd(dx, dy)
                    a = dy // g
                    b = dx // g
                    if b < 0:
                        a, b = -a, -b

                c = b * y1 - a * x1
                dt[(a, b)][c] = dt[(a, b)].get(c, 0) + 1

                mx, my = x1 + x2, y1 + y2
                dm[(mx, my)][(a, b)] = dm[(mx, my)].get((a, b), 0) + 1

        ans = 0
        for v in dt.values():
            tot = sum(v.values())
            ans += tot * (tot - 1) // 2
            for cnt in v.values():
                ans -= cnt * (cnt - 1) // 2

        for v in dm.values():
            tot = sum(v.values())
            ans -= tot * (tot - 1) // 2
            for cnt in v.values():
                ans += cnt * (cnt - 1) // 2

        return ans
